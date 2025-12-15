# Quickstart Guide: RAG Chatbot for Physical AI Book

## Overview
This guide provides a quick setup and deployment process for the RAG chatbot system.

## Prerequisites
- Python 3.10+
- Node.js 18+ (for frontend development)
- Git
- API keys for:
  - Cohere (for embeddings)
  - Google AI (for Gemini)
  - Qdrant Cloud (for vector database)
  - Neon Postgres (for structured data)

## Setup Instructions

### 1. Clone and Navigate to Project
```bash
git clone <your-repo-url>
cd humanoid-robotics-book
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd chatbot/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file from template
cp .env.example .env
# Edit .env with your API keys
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd chatbot/frontend

# Install dependencies
npm install
```

### 4. Environment Configuration
Create `.env` file in `chatbot/backend/` with:
```env
COHERE_API_KEY=your_cohere_api_key
GOOGLE_AI_API_KEY=your_google_ai_api_key
QDRANT_URL=your_qdrant_cluster_url
QDRANT_API_KEY=your_qdrant_api_key
NEON_DATABASE_URL=your_neon_postgres_connection_string
SECRET_KEY=your_secret_key_for_session_management
ALLOWED_ORIGINS=http://localhost:3000,https://your-book-domain.com
```

### 5. Initialize Vector Database
```bash
# From chatbot/backend directory
python ../scripts/ingest.py
```

### 6. Start Backend Server
```bash
# From chatbot/backend directory
uvicorn main:app --reload --port 8000
```

### 7. Start Frontend Development Server
```bash
# From chatbot/frontend directory
npm run dev
```

### 8. Integrate with Docusaurus
Edit `src/theme/Root.js` in the main project to include the chat widget:

```javascript
import React, { useEffect } from 'react';
import { ChatWidget } from '../../chatbot/frontend/src/ChatWidget';

export default function Root({ children }) {
  return (
    <>
      {children}
      <ChatWidget />
    </>
  );
}
```

## API Endpoints

### Chat Endpoint
- **POST** `/chat`
- Request: `{question: string, selected_text?: string, session_id?: string}`
- Response: `{answer: string, sources: array, session_id: string}`

### Ingest Endpoint
- **POST** `/ingest`
- Request: `{force?: boolean}`
- Response: `{chunks_processed: number, status: string, message: string}`

### Health Check
- **GET** `/health`
- Response: `{status: string, timestamp: string, version: string}`

## Running Tests
```bash
# Backend tests
cd chatbot/backend
python -m pytest

# Frontend tests
cd chatbot/frontend
npm test
```

## Building for Production
```bash
# Backend (deploy to Railway/Render)
# Follow deployment instructions in DEPLOYMENT.md

# Frontend (build for Docusaurus integration)
cd chatbot/frontend
npm run build
```

## Troubleshooting

### Common Issues
1. **API Keys**: Ensure all API keys are correctly set in the `.env` file
2. **CORS**: Check `ALLOWED_ORIGINS` in your environment variables
3. **Database Connection**: Verify Neon Postgres connection string format
4. **Vector Database**: Ensure Qdrant cluster is accessible and API key is valid

### Checking System Health
```bash
curl http://localhost:8000/health
```