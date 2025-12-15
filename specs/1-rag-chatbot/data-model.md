# Data Model: RAG Chatbot for Physical AI Book

## Overview
Data model for the Retrieval-Augmented Generation chatbot system, focusing on the structured data stored in Neon Postgres and the vector data in Qdrant.

## Database Schema (Neon Postgres)

### chat_sessions table
Stores information about individual chat sessions

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key, auto-incrementing ID |
| user_id | TEXT | Identifier for the user (browser session-based) |
| created_at | TIMESTAMP | When the session was created |

### chat_messages table
Stores individual question-answer pairs within sessions

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key, auto-incrementing ID |
| session_id | INTEGER | Foreign key referencing chat_sessions.id |
| question | TEXT | The user's original question |
| answer | TEXT | The AI-generated answer |
| selected_text | TEXT | The text the user had selected when asking (nullable) |
| sources | TEXT[] | Array of source URLs referenced in the answer |
| created_at | TIMESTAMP | When the message was created |

## Vector Database Schema (Qdrant)

### book_content collection
Stores text chunks with embeddings for semantic search

**Vector Configuration:**
- Vector size: 1024 (Cohere embed-english-v3.0 large size)
- Distance: Cosine

**Payload Structure:**
- text: string (the actual text chunk content)
- url: string (source page URL)
- page_title: string (title of the source page)
- chunk_index: integer (position of chunk in the original page)
- book_section: string (which section of the book this belongs to)

## API Data Models

### Request Models

**Chat Request (POST /chat)**
```json
{
  "question": "string (required)",
  "selected_text": "string (optional)",
  "session_id": "string (optional)"
}
```

**Ingest Request (POST /ingest)**
```json
{
  "force": "boolean (optional, default: false)"
}
```

### Response Models

**Chat Response (POST /chat)**
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
  "session_id": "string"
}
```

**Ingest Response (POST /ingest)**
```json
{
  "chunks_processed": "integer",
  "status": "string",
  "message": "string"
}
```

**Health Response (GET /health)**
```json
{
  "status": "string (healthy|unhealthy)",
  "timestamp": "string (ISO 8601)",
  "version": "string"
}
```

## Frontend State Models

### Chat Message Object
```typescript
interface ChatMessage {
  id: string;
  type: 'user' | 'assistant';
  content: string;
  sources?: Array<{
    url: string;
    title: string;
    content: string;
  }>;
  timestamp: Date;
  selectedText?: string;
}
```

### Chat Session Object
```typescript
interface ChatSession {
  id: string;
  messages: ChatMessage[];
  createdAt: Date;
}
```

## Validation Rules

### Input Validation
- Question length: 1-2000 characters
- Selected text length: 0-5000 characters
- Session ID format: UUID v4 format if provided

### Content Validation
- All user inputs sanitized to prevent injection
- URLs in sources are validated for proper format
- Source attribution limited to 5 sources per response

### Rate Limiting
- Maximum 10 requests per minute per IP
- Burst allowance of 3 requests