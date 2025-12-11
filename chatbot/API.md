# API Documentation: RAG Chatbot for Physical AI Book

## Base URL
```
https://your-deployed-backend.com
```

## Authentication
Some endpoints require an API key in the header:
```
X-API-Key: your-api-key-here
```

## Endpoints

### POST /chat
Process a user question and return an AI-generated answer with source attribution.

#### Request
```json
{
  "question": "string (required)",
  "selected_text": "string (optional)",
  "session_id": "string (optional)"
}
```

#### Response (200 OK)
```json
{
  "answer": "string",
  "sources": [
    {
      "url": "string",
      "title": "string",
      "content": "string (relevant excerpt)"
    }
  ],
  "session_id": "string",
  "confidence": "number (optional)"
}
```

#### Error Responses
- `400 Bad Request`: Invalid request parameters
- `500 Internal Server Error`: Server error during processing

#### Example Request
```bash
curl -X POST https://your-api.com/chat \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is ROS 2 and how does it differ from ROS 1?",
    "selected_text": "ROS 2 is a next-generation robotics framework...",
    "session_id": "sess_abc123def456"
  }'
```

### POST /ingest
Ingest book content to vector database from sitemap.

#### Request
```json
{
  "sitemap_url": "string (required)",
  "force": "boolean (optional, default: false)"
}
```

#### Response (200 OK)
```json
{
  "chunks_processed": "integer",
  "status": "string",
  "message": "string"
}
```

#### Error Responses
- `401 Unauthorized`: Invalid API key
- `500 Internal Server Error`: Server error during ingestion

### GET /health
Health check endpoint to verify service status.

#### Response (200 OK)
```json
{
  "status": "healthy",
  "timestamp": "string (ISO 8601)",
  "version": "string"
}
```

### GET /stats
Get usage statistics for analytics.

#### Response (200 OK)
```json
{
  "total_questions": "integer",
  "active_sessions": "integer",
  "avg_response_time": "number",
  "success_rate": "number"
}
```

#### Error Responses
- `401 Unauthorized`: Invalid API key

## Rate Limiting
- Maximum 10 requests per minute per IP
- Burst allowance of 3 requests

## Error Format
All error responses follow this format:
```json
{
  "error": "string (error code)",
  "message": "string (human-readable message)",
  "details": "object (optional, additional error details)"
}
```

## Common Error Codes
- `INVALID_INPUT`: Request parameters are invalid
- `EMBEDDING_ERROR`: Error generating embeddings
- `VECTOR_SEARCH_ERROR`: Error searching vector database
- `LLM_ERROR`: Error with language model
- `DATABASE_ERROR`: Error accessing database
- `CONTENT_NOT_FOUND`: No relevant content found for question

## Request Guidelines
- Question length: 1-2000 characters
- Selected text length: 0-5000 characters
- Session ID format: UUID v4 (if provided)

## Response Time Expectations
- Most requests should complete within 5 seconds
- Complex queries may take up to 10 seconds
- Vector search operations typically complete within 500ms