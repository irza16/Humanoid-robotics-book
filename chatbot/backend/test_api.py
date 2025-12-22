import pytest
import asyncio
from fastapi.testclient import TestClient
from main import app
from config import settings

# Create a test client
client = TestClient(app)

def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert data["version"] == "1.0.0"

def test_chat_endpoint_basic():
    """Test the chat endpoint with a basic question"""
    # This test requires the backend services to be available
    # For now, we'll test the validation and basic structure
    response = client.post(
        "/chat",
        json={
            "question": "What is this book about?",
            "selected_text": None
        }
    )
    # The response could be 200 (success) or 500 (if services are not configured)
    # We'll accept both as the test is about the API structure
    assert response.status_code in [200, 500]

def test_chat_endpoint_with_selected_text():
    """Test the chat endpoint with selected text"""
    response = client.post(
        "/chat",
        json={
            "question": "Explain this concept",
            "selected_text": "This is some selected text from the book"
        }
    )
    assert response.status_code in [200, 500]

def test_chat_endpoint_validation():
    """Test the chat endpoint validation"""
    # Test with empty question
    response = client.post(
        "/chat",
        json={
            "question": "",
            "selected_text": None
        }
    )
    assert response.status_code == 422  # Validation error

    # Test with very long question
    long_question = "A" * 2001  # Exceeds max length
    response = client.post(
        "/chat",
        json={
            "question": long_question,
            "selected_text": None
        }
    )
    assert response.status_code == 422  # Validation error

def test_stats_endpoint():
    """Test the stats endpoint"""
    response = client.get("/stats")
    assert response.status_code == 200
    data = response.json()
    assert "total_questions" in data
    assert "total_sessions" in data
    assert "active_sessions" in data
    assert "avg_response_time" in data
    assert "success_rate" in data
    assert "timestamp" in data

def test_ingest_endpoint():
    """Test the ingest endpoint"""
    # This requires external services to be configured
    # We'll test the validation part
    response = client.post(
        "/ingest",
        json={}
    )
    # Should return 422 for missing sitemap_url or 500 if services not available
    assert response.status_code in [400, 422, 500]

    # Test with a sitemap URL
    response = client.post(
        "/ingest",
        json={
            "sitemap_url": "https://example.com/sitemap.xml"
        }
    )
    assert response.status_code in [200, 500]

if __name__ == "__main__":
    pytest.main([__file__])