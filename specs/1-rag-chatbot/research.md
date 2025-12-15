# Research: RAG Chatbot for Physical AI Book

## Overview
Research document for implementing a Retrieval-Augmented Generation (RAG) chatbot embedded in the Physical AI & Humanoid Robotics book Docusaurus site.

## Technology Decisions & Rationale

### 1. Embedding Model: Cohere embed-english-v3.0

**Decision**: Use Cohere embed-english-v3.0 for text embeddings
**Rationale**:
- Free tier available with good performance
- High dimensional embeddings (1024/768/512 dimensions depending on type)
- Specifically optimized for English text, which matches the book content
- Well-documented API with good Python client support
- Good semantic search performance for technical content

**Alternatives considered**:
- OpenAI text-embedding-ada-002: Costlier than Cohere free tier
- Sentence Transformers: Self-hosted option but requires more infrastructure
- Google embeddings: Different pricing model, less optimized for RAG

### 2. LLM: Google Gemini-2.5-flash

**Decision**: Use Google Gemini-2.5-flash for answer generation
**Rationale**:
- Very fast response times (critical for chatbot UX)
- Free tier available during development
- Excellent for RAG applications with good context handling
- Strong performance on technical content
- Good safety and content filtering

**Alternatives considered**:
- OpenAI GPT models: Costlier than Gemini free tier
- Anthropic Claude: Also good but different pricing model
- Mistral/Azure: Different ecosystem integration

### 3. Vector Database: Qdrant Cloud

**Decision**: Use Qdrant Cloud for vector storage and semantic search
**Rationale**:
- Excellent performance for semantic search
- Cloud-hosted with good reliability
- Python client library with good documentation
- Supports metadata storage for source attribution
- Free tier available for development

**Alternatives considered**:
- Pinecone: Good alternative but different pricing
- Weaviate: Open source option but self-hosting complexity
- Chroma: Simpler but less scalable for production

### 4. Backend Framework: FastAPI

**Decision**: Use FastAPI for the backend API
**Rationale**:
- Fast, modern Python web framework with async support
- Automatic API documentation (Swagger/OpenAPI)
- Excellent for ML/AI API development
- Strong validation and error handling
- Good integration with Python ML ecosystem

**Alternatives considered**:
- Flask: Simpler but less modern features
- Django: More complex than needed for API
- Express.js: Would require changing to Node.js ecosystem

### 5. Frontend Integration: React Widget in Docusaurus

**Decision**: Create a React chat widget embedded in Docusaurus via theme customization
**Rationale**:
- React provides good component architecture for chat interface
- Can be embedded in Docusaurus via Root.js theme customization
- TypeScript support for better development experience
- Good for handling selected text detection and UX
- Familiar to developers

**Alternatives considered**:
- Vanilla JavaScript: Less structured, harder to maintain
- Vue/Svelte: Different ecosystem than React
- Pure CSS/HTML widget: Less interactive capability

## Architecture Research

### RAG Pipeline Design

**Step 1: Ingestion**
- Extract text from book pages using sitemap.xml
- Chunk text using sentence-aware chunking with overlap
- Generate embeddings using Cohere
- Store in Qdrant with metadata (URL, page title, chunk index)

**Step 2: Retrieval**
- Convert user query to embedding
- Search Qdrant for top 3-5 similar chunks
- If user selected text, boost relevance for that content
- Return relevant chunks with source metadata

**Step 3: Generation**
- Build prompt with retrieved context + user query
- Use Gemini-2.5-flash to generate answer
- Include source attribution in response
- Return structured response with answer and sources

**Step 4: Storage**
- Store user queries and responses in Neon Postgres
- Link to session for analytics
- Store selected text if provided

### Selected Text Handling

**Mechanism**: Use JavaScript `window.getSelection()` API to detect selected text
**Integration**:
- Add event listener for text selection
- Detect when user has selected text and opens chat
- Pass selected text as context to backend
- Highlight in UI that selected text is being referenced

## API Design Research

### Backend Endpoints

**POST /chat**
- Request: `{question: string, selected_text?: string, session_id?: string}`
- Response: `{answer: string, sources: Array<{url: string, title: string, content: string}>}`
- Error handling for invalid requests, API failures

**POST /ingest**
- Request: `{force?: boolean}`
- Response: `{chunks_processed: number, status: string}`
- For ingesting book content to Qdrant

**GET /health**
- Request: None
- Response: `{status: "healthy", timestamp: string}`

## Security Considerations

### Input Validation
- Sanitize all user inputs to prevent injection attacks
- Validate question length and content
- Rate limiting on API endpoints

### Data Privacy
- Don't store personally identifiable information
- Session-based approach without user accounts
- Clear data retention policy

### API Security
- Environment-based API key management
- CORS configuration limited to book domain
- HTTPS enforcement

## Performance Optimization

### Response Time
- Use Gemini-2.5-flash for fast responses
- Optimize chunk size (1000-1500 chars) for search quality
- Cache common queries if needed
- Async processing where possible

### Frontend Performance
- Lazy loading of chat widget
- Minimal impact on page load time
- Efficient state management
- Mobile-optimized design

## Deployment Strategy

### Backend Deployment
- Deploy to Railway for free tier hosting
- Environment variable configuration
- Health checks and monitoring

### Frontend Integration
- Embed in Docusaurus via theme customization
- CDN hosting of static assets
- Versioned releases to avoid breaking changes

## Risk Mitigation

### API Limits
- Implement retry logic with exponential backoff
- Fallback to alternative models if primary unavailable
- Caching for common queries

### Data Scale
- Monitor Qdrant collection size
- Optimize chunking strategy to balance quality and performance
- Implement pagination for large result sets

### Mobile Compatibility
- Test selected text detection on mobile browsers
- Provide alternative input methods if needed
- Responsive design for chat interface