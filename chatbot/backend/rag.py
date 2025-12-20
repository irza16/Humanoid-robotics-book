import os
from typing import List, Dict, Optional, Tuple
import logging
import time
from config import settings

# Import OpenAI API components
from openai import OpenAI
import json
import cohere
from qdrant_client import QdrantClient

# Import retry utility
from retry_utils import retry_with_backoff

logger = logging.getLogger(__name__)


@retry_with_backoff(
    max_retries=3,
    base_delay=1.0,
    max_delay=10.0,
    exceptions=(Exception,)
)
def retrieve_content(query: str) -> List[Dict]:
    """Retrieve relevant book content chunks based on the query"""
    try:
        # Initialize Cohere client
        cohere_client = cohere.Client(settings.cohere_api_key)

        # Initialize Qdrant client
        qdrant = QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key
        )

        # Generate embedding for the query
        embedding = cohere_client.embed(
            model=settings.embedding_model,
            input_type="search_query",
            texts=[query]
        ).embeddings[0]

        # Search in Qdrant
        results = qdrant.query_points(
            collection_name="book_content",
            query=embedding,
            limit=settings.top_k_chunks
        )

        # Extract text content and metadata from results
        retrieved_docs = []
        for point in results.points:
            payload = point.payload
            doc_info = {
                "text": payload.get("text", ""),
                "url": payload.get("url", ""),
                "title": payload.get("title", ""),
                "score": point.score  # Similarity score
            }
            retrieved_docs.append(doc_info)

        return retrieved_docs
    except Exception as e:
        logger.error(f"Error in retrieve function: {str(e)}")
        return []


class RAGPipeline:
    def __init__(self):
        # Initialize the OpenAI client with Gemini via OpenAI SDK
        self.client = OpenAI(
            api_key=settings.gemini_api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

    def process_query(self, question: str, selected_text: Optional[str] = None) -> Tuple[str, List[Dict]]:
        """Main method to process a user query through the RAG pipeline"""
        start_time = time.time()

        try:
            logger.info(f"Processing query: {question[:50]}...")

            # First, retrieve relevant documents to get the sources
            query_text = f"{selected_text} {question}" if selected_text else question
            retrieved_docs = retrieve_content(query_text)

            # Build the context from retrieved documents
            context_texts = []
            for i, doc in enumerate(retrieved_docs[:3]):  # Use top 3 documents
                context_texts.append(f"Source {i+1}: {doc['text'][:500]}...")

            context_str = "\n".join(context_texts)

            # Build the prompt based on whether selected text is provided
            if selected_text:
                system_prompt = f"""
                You are a helpful tutor for the Physical AI & Humanoid Robotics book.
                Use the following retrieved content as context to answer the user's question.
                Always provide answers based ONLY on the provided context.
                If the answer is not available in the context, say so clearly.

                Retrieved content for context:
                {context_str}
                """

                user_prompt = f"""
                User has selected text: {selected_text}

                Question: {question}

                Please answer the question focusing on the selected text and using the retrieved content as context.
                """
            else:
                system_prompt = f"""
                You are a helpful tutor for the Physical AI & Humanoid Robotics book.
                Use the following retrieved content as context to answer the user's question.
                Always provide answers based ONLY on the provided context.
                If the answer is not available in the context, say so clearly.

                Retrieved content for context:
                {context_str}
                """

                user_prompt = f"""
                Question: {question}

                Please answer the question using the retrieved content as context.
                """

            # Call the OpenAI-compatible API (Gemini)
            response = self.client.chat.completions.create(
                model=settings.llm_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=settings.temperature,
                max_tokens=settings.max_tokens
            )

            # Extract the answer from the response
            answer = response.choices[0].message.content if response.choices else "I don't have information about that in the book."

            # Format the sources from the retrieved documents
            sources = []
            for doc in retrieved_docs:
                if doc.get('url'):
                    source = {
                        "url": doc.get("url", ""),
                        "title": doc.get("title", ""),
                        "content": doc.get("text", "")[:200] + "..." if len(doc.get("text", "")) > 200 else doc.get("text", ""),
                        "score": doc.get("score", 0.0)
                    }
                    sources.append(source)

            logger.info(f"Query processed successfully in {time.time() - start_time:.2f}s")
            return answer, sources

        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            raise


# Global RAG pipeline instance
rag_pipeline = None


def init_rag_pipeline():
    """Initialize the RAG pipeline"""
    global rag_pipeline
    rag_pipeline = RAGPipeline()


def get_rag_pipeline() -> RAGPipeline:
    """Get the RAG pipeline instance"""
    global rag_pipeline
    if rag_pipeline is None:
        raise RuntimeError("RAG pipeline not initialized")
    return rag_pipeline