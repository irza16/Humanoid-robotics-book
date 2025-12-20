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
                You are an expert tutor for the Physical AI & Humanoid Robotics book. Provide comprehensive, well-structured answers using complete sentences. Do not repeat information unnecessarily. Base all answers strictly on the provided context. If information is not available in the context, clearly state this. Organize your response logically with clear explanations.

                Retrieved content for context:
                {context_str}
                """

                user_prompt = f"""
                User has selected text: {selected_text}

                Question: {question}

                Answer the question thoroughly, focusing on the selected text and using the retrieved content as context. Provide detailed explanations in complete sentences without unnecessary repetition.
                """
            else:
                system_prompt = f"""
                You are an expert tutor for the Physical AI & Humanoid Robotics book. Provide comprehensive, well-structured answers using complete sentences. Do not repeat information unnecessarily. Base all answers strictly on the provided context. If information is not available in the context, clearly state this. Organize your response logically with clear explanations.

                Retrieved content for context:
                {context_str}
                """

                user_prompt = f"""
                Question: {question}

                Answer the question thoroughly using the retrieved content as context. Provide detailed explanations in complete sentences without unnecessary repetition.
                """

            # Call the OpenAI-compatible API (Gemini) with increased max_tokens for better answers
            response = self.client.chat.completions.create(
                model=settings.llm_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=settings.temperature,
                max_tokens=800  # Increased from default to allow more comprehensive answers
            )

            # Extract the answer from the response with proper error handling
            if response and hasattr(response, 'choices') and response.choices:
                choice = response.choices[0]
                if choice and hasattr(choice, 'message') and choice.message:
                    answer = choice.message.content if hasattr(choice.message, 'content') else "I don't have information about that in the book."
                else:
                    answer = "I don't have information about that in the book."
            else:
                answer = "I don't have information about that in the book."

            # Format the sources from the retrieved documents
            sources = []
            for doc in retrieved_docs:
                if doc.get('url'):
                    source = {
                        "url": doc.get("url", "") or "",
                        "title": doc.get("title", "") or "",
                        "content": (doc.get("text", "") or "")[:200] + "..." if len(doc.get("text", "") or "") > 200 else (doc.get("text", "") or ""),
                        "score": doc.get("score", 0.0) or 0.0
                    }
                    sources.append(source)

            logger.info(f"Query processed successfully in {time.time() - start_time:.2f}s")
            return answer, sources

        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            raise

    def _remove_duplicate_sentences(self, text: str) -> str:
        """Remove duplicate sentences from the generated text"""
        if not text:
            return text

        import re
        # Split text into sentences
        sentences = re.split(r'(?<=[.!?])\s+', text)

        # Remove duplicates while preserving order
        seen = set()
        unique_sentences = []
        for sentence in sentences:
            # Normalize the sentence for comparison
            normalized = re.sub(r'\s+', ' ', sentence.strip().lower())
            if normalized and normalized not in seen:
                seen.add(normalized)
                unique_sentences.append(sentence.strip())

        return ' '.join(unique_sentences)


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