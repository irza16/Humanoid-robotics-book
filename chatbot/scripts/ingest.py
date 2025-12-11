#!/usr/bin/env python3
"""
Script to ingest book content to Qdrant vector database
This script will:
1. Fetch all pages from sitemap.xml
2. Extract clean text using trafilatura
3. Chunk text into 1000-1500 character segments
4. Generate embeddings using Cohere
5. Store in Qdrant with metadata
"""

import os
import requests
import trafilatura
from urllib.parse import urljoin, urlparse
from dotenv import load_dotenv
import cohere
from qdrant_client import QdrantClient
from qdrant_client.http import models
import time
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BookIngestor:
    def __init__(self):
        self.cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))
        self.qdrant_client = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY")
        )

        # Initialize Qdrant collection for book content
        self.collection_name = "book_content"
        self._init_collection()

    def _init_collection(self):
        """Initialize Qdrant collection with proper vector configuration"""
        try:
            # Check if collection exists
            self.qdrant_client.get_collection(self.collection_name)
            logger.info(f"Collection {self.collection_name} already exists")
        except:
            # Create collection with 1024-dimensional vectors (Cohere embed-english-v3.0 large)
            self.qdrant_client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE),
            )
            logger.info(f"Created collection {self.collection_name} with 1024-dimensional vectors")

    def fetch_sitemap(self, sitemap_url: str) -> list:
        """Fetch and parse sitemap.xml to extract all page URLs"""
        logger.info(f"Fetching sitemap from {sitemap_url}")

        response = requests.get(sitemap_url)
        response.raise_for_status()

        # Simple XML parsing for sitemap URLs
        import xml.etree.ElementTree as ET
        root = ET.fromstring(response.content)

        urls = []
        for url_element in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
            loc = url_element.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
            if loc is not None:
                urls.append(loc.text)

        logger.info(f"Found {len(urls)} URLs in sitemap")
        return urls

    def extract_text_from_url(self, url: str) -> str:
        """Extract clean text content from a URL using trafilatura"""
        logger.info(f"Extracting text from {url}")

        try:
            downloaded = requests.get(url, timeout=10)
            downloaded.raise_for_status()

            text = trafilatura.extract(downloaded.text)
            return text or ""
        except Exception as e:
            logger.error(f"Error extracting text from {url}: {str(e)}")
            return ""

    def chunk_text(self, text: str, max_chunk_size: int = 1000, overlap: int = 200) -> list:
        """Chunk text into overlapping segments of specified size"""
        if not text:
            return []

        chunks = []
        start = 0

        while start < len(text):
            end = start + max_chunk_size

            # If we're near the end, just take the remaining text
            if end > len(text):
                end = len(text)
            else:
                # Try to break at sentence boundary
                while end < len(text) and text[end] not in '.!?':
                    end += 1
                if end < len(text):
                    end += 1  # Include the punctuation

            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)

            # Move start to the next position with overlap
            start = end - overlap if end < len(text) else len(text)

        return chunks

    def generate_embeddings(self, texts: list) -> list:
        """Generate embeddings for a list of texts using Cohere"""
        if not texts:
            return []

        logger.info(f"Generating embeddings for {len(texts)} text chunks")

        # Cohere batch embedding generation (max 96 texts per request)
        batch_size = 96
        all_embeddings = []

        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            response = self.cohere_client.embed(
                texts=batch,
                model="embed-english-v3.0",
                input_type="search_document"
            )
            all_embeddings.extend(response.embeddings)

        return all_embeddings

    def store_in_qdrant(self, chunks: list, urls: list, titles: list):
        """Store text chunks with embeddings in Qdrant"""
        logger.info(f"Storing {len(chunks)} chunks in Qdrant")

        # Generate all embeddings at once for efficiency
        embeddings = self.generate_embeddings(chunks)

        points = []
        for i, (chunk, url, title, embedding) in enumerate(zip(chunks, urls, titles, embeddings)):
            point = models.PointStruct(
                id=i,
                vector=embedding,
                payload={
                    "text": chunk,
                    "url": url,
                    "page_title": title,
                    "chunk_index": i,
                    "book_section": "unknown"  # This would be determined based on URL structure
                }
            )
            points.append(point)

        # Upload points to Qdrant
        self.qdrant_client.upsert(
            collection_name=self.collection_name,
            points=points
        )

        logger.info(f"Successfully stored {len(points)} points in Qdrant")

    def ingest_book_content(self, sitemap_url: str, force: bool = False):
        """Main method to ingest book content from sitemap"""
        logger.info("Starting book content ingestion process")

        # Fetch all URLs from sitemap
        urls = self.fetch_sitemap(sitemap_url)

        all_chunks = []
        all_urls = []
        all_titles = []

        for url in urls:
            # Extract text from URL
            text = self.extract_text_from_url(url)
            if not text:
                continue

            # Extract page title (simplified)
            title = urlparse(url).path.split('/')[-1] or "Untitled"

            # Chunk the text
            chunks = self.chunk_text(text)

            # Add to collections
            for chunk in chunks:
                all_chunks.append(chunk)
                all_urls.append(url)
                all_titles.append(title)

        # Store in Qdrant
        self.store_in_qdrant(all_chunks, all_urls, all_titles)

        logger.info(f"Ingestion completed. Processed {len(all_chunks)} chunks from {len(urls)} pages")


def main():
    """Main function to run the ingestion script"""
    import argparse

    parser = argparse.ArgumentParser(description="Ingest book content to Qdrant")
    parser.add_argument("--sitemap-url", required=True, help="URL to the sitemap.xml")
    parser.add_argument("--force", action="store_true", help="Force re-ingestion even if content exists")

    args = parser.parse_args()

    # Initialize the ingestor
    ingestor = BookIngestor()

    # Run the ingestion process
    ingestor.ingest_book_content(args.sitemap_url, args.force)


if __name__ == "__main__":
    main()