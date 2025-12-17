"""Reusable agent skills for the multi-agent RAG chatbot system."""

from typing import List, Dict, Optional
import logging
from functools import wraps
from config import settings
import cohere
from qdrant_client import QdrantClient
from retry_utils import retry_with_backoff

logger = logging.getLogger(__name__)


def function_tool(func):
    """Decorator to mark functions as agent tools."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.is_tool = True
    return wrapper


def _get_qdrant_client():
    """Helper function to get Qdrant client instance."""
    return QdrantClient(
        url=settings.qdrant_url,
        api_key=settings.qdrant_api_key
    )


def _get_cohere_client():
    """Helper function to get Cohere client instance."""
    return cohere.Client(settings.cohere_api_key)


@function_tool
@retry_with_backoff(
    max_retries=3,
    base_delay=1.0,
    max_delay=10.0,
    exceptions=(Exception,)
)
def search_module_content(module_name: str, query: str) -> List[str]:
    """Search specific module content in Qdrant.

    Args:
        module_name: Name of the module to search in (e.g., 'module-1-ros2')
        query: User question to search for

    Returns:
        List of relevant text chunks from the specified module
    """
    try:
        # Initialize Cohere client
        cohere_client = _get_cohere_client()

        # Initialize Qdrant client
        qdrant = _get_qdrant_client()

        # Generate embedding for the query
        embedding = cohere_client.embed(
            model=settings.embedding_model,
            input_type="search_query",
            texts=[query]
        ).embeddings[0]

        # Search in the specific module collection
        collection_name = f"book_content_{module_name}"
        results = qdrant.query_points(
            collection_name=collection_name,
            query=embedding,
            limit=settings.top_k_chunks
        )

        # Extract text content from results
        retrieved_texts = []
        for point in results.points:
            payload = point.payload
            text = payload.get("text", "")
            if text:
                retrieved_texts.append(text)

        logger.info(f"Found {len(retrieved_texts)} results for query in {collection_name}")
        return retrieved_texts

    except Exception as e:
        logger.error(f"Error in search_module_content: {str(e)}")
        # Fallback to general search if module-specific collection doesn't exist
        return _fallback_search(query)


@function_tool
@retry_with_backoff(
    max_retries=3,
    base_delay=1.0,
    max_delay=10.0,
    exceptions=(Exception,)
)
def find_code_examples(topic: str, language: Optional[str] = None) -> List[str]:
    """Find code snippets related to a specific topic.

    Args:
        topic: Topic to search for code examples (e.g., 'ROS 2 publisher')
        language: Optional language filter (e.g., 'python', 'cpp')

    Returns:
        List of code examples from the book
    """
    try:
        # Initialize Cohere client
        cohere_client = _get_cohere_client()

        # Initialize Qdrant client
        qdrant = _get_qdrant_client()

        # Create search query for code examples
        if language:
            query = f"code example {topic} {language}"
        else:
            query = f"code example {topic}"

        # Generate embedding for the query
        embedding = cohere_client.embed(
            model=settings.embedding_model,
            input_type="search_query",
            texts=[query]
        ).embeddings[0]

        # Search in the general book content collection
        results = qdrant.query_points(
            collection_name="book_content",
            query=embedding,
            limit=settings.top_k_chunks
        )

        # Extract text content that likely contains code examples
        code_examples = []
        for point in results.points:
            payload = point.payload
            text = payload.get("text", "")
            # Look for code-like patterns in the text
            if text and ('```' in text or 'def ' in text or 'class ' in text or
                         'import ' in text or 'ros2' in text.lower() or
                         'launch' in text.lower() or 'node' in text.lower()):
                code_examples.append(text)

        logger.info(f"Found {len(code_examples)} code examples for topic: {topic}")
        return code_examples

    except Exception as e:
        logger.error(f"Error in find_code_examples: {str(e)}")
        return []


@function_tool
@retry_with_backoff(
    max_retries=3,
    base_delay=1.0,
    max_delay=10.0,
    exceptions=(Exception,)
)
def get_prerequisites(topic: str) -> str:
    """Get prerequisite knowledge for a specific topic.

    Args:
        topic: Topic to get prerequisites for (e.g., 'URDF', 'VSLAM')

    Returns:
        Prerequisite information for the topic
    """
    try:
        # Initialize Cohere client
        cohere_client = _get_cohere_client()

        # Initialize Qdrant client
        qdrant = _get_qdrant_client()

        # Create search query for prerequisites
        query = f"prerequisites for {topic} what to learn before {topic}"

        # Generate embedding for the query
        embedding = cohere_client.embed(
            model=settings.embedding_model,
            input_type="search_query",
            texts=[query]
        ).embeddings[0]

        # Search in the general book content collection
        results = qdrant.query_points(
            collection_name="book_content",
            query=embedding,
            limit=settings.top_k_chunks
        )

        # Extract prerequisite information
        prerequisites_text = []
        for point in results.points:
            payload = point.payload
            text = payload.get("text", "")
            if text and ('prerequisite' in text.lower() or 'before' in text.lower() or
                         'first' in text.lower() or 'require' in text.lower() or
                         'need to' in text.lower() or 'understand' in text.lower()):
                prerequisites_text.append(text)

        if prerequisites_text:
            return " ".join(prerequisites_text[:2])  # Return first 2 relevant chunks
        else:
            return f"No specific prerequisites found for {topic}. General robotics and programming knowledge is recommended."

    except Exception as e:
        logger.error(f"Error in get_prerequisites: {str(e)}")
        return f"Unable to determine prerequisites for {topic}. General robotics and programming knowledge is recommended."


@function_tool
@retry_with_backoff(
    max_retries=3,
    base_delay=1.0,
    max_delay=10.0,
    exceptions=(Exception,)
)
def explain_concept(concept: str) -> str:
    """Get detailed explanation of a core concept.

    Args:
        concept: Concept to explain (e.g., 'URDF', 'VSLAM', 'TF2')

    Returns:
        Comprehensive explanation of the concept
    """
    try:
        # Initialize Cohere client
        cohere_client = _get_cohere_client()

        # Initialize Qdrant client
        qdrant = _get_qdrant_client()

        # Create search query for concept explanation
        query = f"what is {concept} definition explanation {concept}"

        # Generate embedding for the query
        embedding = cohere_client.embed(
            model=settings.embedding_model,
            input_type="search_query",
            texts=[query]
        ).embeddings[0]

        # Search in the general book content collection
        results = qdrant.query_points(
            collection_name="book_content",
            query=embedding,
            limit=settings.top_k_chunks
        )

        # Extract explanation text
        explanation_texts = []
        for point in results.points:
            payload = point.payload
            text = payload.get("text", "")
            if text:
                explanation_texts.append(text)

        if explanation_texts:
            return " ".join(explanation_texts[:3])  # Return first 3 relevant chunks
        else:
            return f"No detailed explanation found for {concept} in the book content."

    except Exception as e:
        logger.error(f"Error in explain_concept: {str(e)}")
        return f"Unable to provide a detailed explanation for {concept} at this time."


def _fallback_search(query: str) -> List[str]:
    """Fallback search in the general collection if module-specific collection doesn't exist."""
    try:
        # Initialize Cohere client
        cohere_client = _get_cohere_client()

        # Initialize Qdrant client
        qdrant = _get_qdrant_client()

        # Generate embedding for the query
        embedding = cohere_client.embed(
            model=settings.embedding_model,
            input_type="search_query",
            texts=[query]
        ).embeddings[0]

        # Search in the general book content collection
        results = qdrant.query_points(
            collection_name="book_content",
            query=embedding,
            limit=settings.top_k_chunks
        )

        # Extract text content from results
        retrieved_texts = []
        for point in results.points:
            payload = point.payload
            text = payload.get("text", "")
            if text:
                retrieved_texts.append(text)

        logger.info(f"Fallback search found {len(retrieved_texts)} results for query")
        return retrieved_texts

    except Exception as e:
        logger.error(f"Error in fallback search: {str(e)}")
        return []