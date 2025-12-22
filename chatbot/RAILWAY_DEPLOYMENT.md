# Deployment Guide: RAG Chatbot for Physical AI Book

## Overview
This guide provides step-by-step instructions for deploying the RAG (Retrieval-Augmented Generation) chatbot for the Physical AI & Humanoid Robotics book to Railway. The system consists of a FastAPI backend deployed to Railway and a Docusaurus frontend deployed to GitHub Pages.

## Architecture Components
- **Backend**: FastAPI server hosted on Railway
- **AI Models**: Google Gemini 2.0 Flash via OpenAI SDK
- **Embeddings**: Cohere embed-english-v3.0
- **Vector DB**: Qdrant Cloud
- **Storage**: Neon Postgres for chat history
- **Frontend**: JavaScript widget embedded in Docusaurus

---

## 1. Backend Deployment to Railway

### 1.1 Prerequisites
- Railway account with billing configured
- Valid API keys for:
  - Google Gemini (GEMINI_API_KEY)
  - Cohere (COHERE_API_KEY)
  - Qdrant Cloud (QDRANT_URL and QDRANT_API_KEY)
  - Neon Postgres (NEON_DATABASE_URL)
- GitHub repository with the chatbot code
- Sitemap URL of the book website for content ingestion

### 1.2 Important Note
The backend (FastAPI application) is Python-based and should be deployed to Railway.
The frontend (Docusaurus site) is JavaScript-based and is typically deployed to GitHub Pages, not Railway.
If you want to deploy the Docusaurus site to Railway as well, it requires Node.js 20+.

### 1.3 Railway Setup Process

#### Step 1: Prepare Repository for Deployment
1. Ensure all dependencies are listed in `chatbot/backend/requirements.txt`
2. Verify `.env.example` contains all required environment variables
3. Confirm `main.py` properly uses environment variables for configuration
4. Make sure the start command is properly configured

#### Step 2: Create New Railway Project
1. Navigate to [Railway.app](https://railway.app)
2. Click "New Project"
3. Choose "Deploy from GitHub"
4. Select your repository containing the chatbot code
5. Railway will automatically detect the Python backend due to the Procfile in the root directory

#### Step 3: Configure Environment Variables in Railway
Add the following environment variables in Railway's Environment Variables section:

```
GEMINI_API_KEY=your_google_gemini_api_key
COHERE_API_KEY=your_cohere_api_key
QDRANT_URL=your_qdrant_cloud_cluster_url
QDRANT_API_KEY=your_qdrant_api_key
NEON_DATABASE_URL=your_neon_postgres_connection_string
SECRET_KEY=a_secure_random_key_of_at_least_32_characters
ALLOWED_ORIGINS=["https://irza16.github.io", "https://www.irza16.github.io", "http://localhost:3000"]
DEBUG=false
```

#### Step 4: Configure Deployment Settings
1. The deployment command is automatically set via the Procfile in the root directory:
   - Start command: `cd chatbot/backend && python -m uvicorn main:app --host 0.0.0.0 --port $PORT`

2. Railway will automatically detect Python and install dependencies from requirements.txt
   - Runtime: Python 3.10+ (detected automatically)
   - Build command: `pip install -r chatbot/backend/requirements.txt` (detected automatically)

#### Step 5: Deploy and Monitor
1. Trigger the initial deployment from the Railway dashboard
2. Monitor the deployment logs for:
   - Successful dependency installation
   - Proper environment variable loading
   - Successful application startup
   - Port binding to $PORT environment variable

#### Step 6: Verify Backend Health
1. Access the `/health` endpoint to confirm the service is running
2. Check the response format matches the expected schema
3. Verify all required services (database connections, AI APIs) are accessible

---

## 2. Required Environment Variables and Configuration

### 2.1 Backend Environment Variables

| Variable | Description | Source |
|----------|-------------|---------|
| `GEMINI_API_KEY` | Google Gemini API key for LLM access | Google AI Studio |
| `COHERE_API_KEY` | Cohere API key for embeddings | Cohere dashboard |
| `QDRANT_URL` | URL of Qdrant Cloud cluster | Qdrant Cloud dashboard |
| `QDRANT_API_KEY` | API key for Qdrant Cloud access | Qdrant Cloud dashboard |
| `NEON_DATABASE_URL` | Connection string for Neon Postgres | Neon dashboard |
| `SECRET_KEY` | Secret key for security operations | Generate securely |
| `ALLOWED_ORIGINS` | Comma-separated list of allowed origins | Your domain configuration |

### 2.2 Security Configuration
- Generate a strong random `SECRET_KEY` (at least 32 characters)
- Restrict `ALLOWED_ORIGINS` to only production and development domains
- Never commit actual API keys to version control
- Use Railway's secure environment variable storage

---

## 3. Database Setup and Content Ingestion Process

### 3.1 Database Preparation
1. **Neon Postgres Setup**:
   - Create a new Neon project
   - Obtain the connection string from the Neon dashboard
   - The application will automatically create required tables on first run

2. **Qdrant Vector Database Setup**:
   - Create a Qdrant Cloud account
   - Create a new cluster
   - Note the cluster URL and API key
   - The application will automatically create the `book_content` collection

### 3.2 Content Ingestion Process

#### Option A: Using API Endpoint (Recommended for Production)
1. Once the backend is deployed and running:
   ```bash
   curl -X POST https://your-railway-app.railway.app/ingest \
     -H "Content-Type: application/json" \
     -d '{
       "sitemap_url": "https://irza16.github.io/Humanoid-robotics-book/sitemap.xml",
       "force": false
     }'
   ```

#### Option B: Using Ingestion Script (For Initial Setup)
1. Clone the repository locally where environment variables are configured
2. Run the ingestion script:
   ```bash
   cd chatbot/scripts
   python ingest.py --sitemap-url "https://irza16.github.io/Humanoid-robotics-book/sitemap.xml"
   ```

#### Content Ingestion Details:
- The process extracts text from all URLs in the sitemap
- Text is chunked into 1000-character segments with 200-character overlap
- Each chunk is embedded using Cohere's embed-english-v3.0 model
- Embedded chunks are stored in Qdrant with metadata (URL, title, etc.)
- The process may take considerable time depending on book size

### 3.3 Ingestion Validation
1. Verify the Qdrant collection has been populated
2. Test the search functionality with sample queries
3. Confirm source attribution works correctly

---

## 4. Frontend Integration

### 4.1 Docusaurus Integration
The chatbot widget is designed to integrate seamlessly with Docusaurus sites:

#### Widget Integration
1. The widget JavaScript (`static/chatbot-widget.js`) is automatically built and placed in the static assets
2. Verify that `src/theme/Root.js` includes the chat widget initialization
3. Ensure the widget is configured to communicate with the deployed backend API

#### Configuration
1. The widget automatically detects if running on localhost vs production
2. In production, it connects to the Railway backend URL
3. The widget includes fallback mechanisms for error handling

---

## 5. Testing and Validation Procedures

### 5.1 Post-Deployment Validation
1. **Health Checks**:
   - Verify `/health` endpoint returns healthy status
   - Check all external service connections are working

2. **Functional Testing**:
   - Test the `/chat` endpoint with various queries
   - Verify source attribution works correctly
   - Test session management functionality
   - Validate selected text functionality

3. **Content Search Testing**:
   - Test queries related to different book sections
   - Verify accurate source attribution
   - Check that responses are contextually relevant

---

## 6. Troubleshooting Steps for Common Issues

### 6.1 Backend Deployment Issues
**Issue**: Application fails to start on Railway
- Check deployment logs for missing dependencies
- Verify all environment variables are properly set
- Confirm the start command matches Railway's requirements

**Issue**: Database connection failures
- Verify the Neon Postgres connection string is correct
- Check that the database is accessible from Railway's network
- Ensure the database credentials are valid

**Issue**: External API connection failures
- Verify API keys are correctly configured
- Check that the services (Gemini, Cohere, Qdrant) are accessible from Railway
- Confirm rate limits are not being exceeded

### 6.2 Frontend Integration Issues
**Issue**: Widget doesn't appear on pages
- Check that the widget JavaScript is properly loaded
- Verify the integration code in `src/theme/Root.js`
- Ensure there are no JavaScript errors in the console

**Issue**: CORS errors when connecting to backend
- Verify `ALLOWED_ORIGINS` includes your GitHub Pages domain
- Check that the backend is returning proper CORS headers
- Confirm the API endpoint URL is correct

### 6.3 Content Search Issues
**Issue**: No relevant results returned
- Verify content has been properly ingested into Qdrant
- Check that the sitemap URL contains all relevant pages
- Confirm embeddings were generated successfully

---

## 7. API Endpoints

### Main Endpoints
- `GET /health` - Health check endpoint
- `POST /chat` - Main chat functionality with selected text support
- `POST /ingest` - Content ingestion from sitemap
- `GET /stats` - Usage statistics

### Request/Response Examples

#### Chat Endpoint
Request:
```json
{
  "question": "What is ROS 2?",
  "selected_text": "Optional selected text from the page",
  "session_id": "Optional session ID"
}
```

Response:
```json
{
  "answer": "Answer to the question...",
  "sources": [
    {
      "url": "https://example.com/source",
      "title": "Source Title",
      "content": "Relevant content snippet..."
    }
  ],
  "session_id": "Session ID"
}
```

---

## 8. Maintenance and Operations

### 8.1 Regular Maintenance Tasks
1. **Content Updates**:
   - Re-run content ingestion when book content is updated
   - Monitor for broken links in source attributions
   - Update sitemap URL as needed

2. **API Key Management**:
   - Monitor usage of paid services (AI APIs, vector DB, hosting)
   - Rotate API keys regularly
   - Update keys in Railway environment variables when needed

### 8.2 Scaling Considerations
1. **Traffic Scaling**:
   - Monitor usage statistics and plan for growth
   - Consider implementing caching for common queries
   - Evaluate the need for additional backend instances

2. **Cost Optimization**:
   - Monitor usage of paid services (AI APIs, vector DB, hosting)
   - Implement cost controls and budget alerts
   - Optimize resource usage where possible

---

## 9. Final Checklist

### Pre-Deployment
- [ ] All environment variables configured securely
- [ ] Database connections tested and verified
- [ ] External API keys validated
- [ ] Content properly ingested into vector database
- [ ] Unit and integration tests passing

### Post-Deployment
- [ ] Backend API accessible and responding
- [ ] Health check endpoint functional
- [ ] Frontend widget loading correctly
- [ ] Chat functionality working end-to-end
- [ ] Source attribution displaying properly
- [ ] Error handling working properly

### Production Validation
- [ ] Load testing completed successfully
- [ ] Security scan passed
- [ ] Performance meets requirements
- [ ] Monitoring alerts configured appropriately

---

## 10. Common Issues and Solutions

### API Quota Issues
If you encounter quota exceeded errors (HTTP 429):
- Check your Google AI and Cohere usage limits
- Consider upgrading to a paid plan for higher quotas
- Implement request caching to reduce API calls

### Deployment Issues
If the application fails to deploy:
- Verify all dependencies are in requirements.txt
- Check that the start command is correct
- Ensure environment variables are properly formatted

### Content Ingestion Issues
If content ingestion fails:
- Verify the sitemap URL is accessible
- Check that the Qdrant connection is working
- Confirm the embedding API keys are valid