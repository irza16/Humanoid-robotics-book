# Deployment Guide: RAG Chatbot for Physical AI Book

## Backend Deployment to Railway

### Prerequisites
- Railway account
- All API keys (Cohere, Google AI, Qdrant, Neon Postgres)

### Steps

1. **Prepare for Railway deployment**
   - Ensure your `requirements.txt` includes all dependencies
   - Make sure `.env.example` has all required environment variables
   - Verify your `main.py` uses environment variables properly

2. **Create a new Railway project**
   - Go to [Railway.app](https://railway.app)
   - Click "New Project"
   - Connect to your GitHub repository or deploy directly

3. **Configure environment variables**
   - Add the following variables in Railway's Environment Variables section:
     ```
     COHERE_API_KEY
     GOOGLE_AI_API_KEY
     QDRANT_URL
     QDRANT_API_KEY
     NEON_DATABASE_URL
     SECRET_KEY
     ALLOWED_ORIGINS
     ```

4. **Set up the deployment command**
   - For the start command, use: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Or create a `Procfile` with: `web: uvicorn main:app --host 0.0.0.0 --port $PORT`

5. **Deploy**
   - Trigger deployment from Railway dashboard
   - Monitor logs to ensure successful deployment

## Frontend Integration

The chat widget is designed to be embedded in your Docusaurus site:

1. **Build the frontend** (if needed as a separate bundle):
   ```bash
   cd chatbot/frontend
   npm run build
   ```

2. **Integrate with Docusaurus**:
   - Add the ChatWidget component to your Docusaurus theme
   - Update `src/theme/Root.js` or create a custom layout

## Environment Configuration

### Backend Environment Variables
```env
COHERE_API_KEY=your_cohere_api_key
GOOGLE_AI_API_KEY=your_google_ai_api_key
QDRANT_URL=your_qdrant_cluster_url
QDRANT_API_KEY=your_qdrant_api_key
NEON_DATABASE_URL=your_neon_postgres_connection_string
SECRET_KEY=a_secure_random_key
ALLOWED_ORIGINS=https://your-book-domain.com,https://www.your-book-domain.com
```

### CORS Configuration
The backend is configured to allow requests from the domains specified in `ALLOWED_ORIGINS`. Make sure to include your production domain.

## Ingesting Content After Deployment

After deploying the backend, you'll need to ingest your book content:

1. **Run the ingestion script**:
   ```bash
   python scripts/ingest.py --sitemap-url "https://your-book-domain.com/sitemap.xml"
   ```

2. **Or use the API endpoint** (if available):
   - POST to `/ingest` endpoint with sitemap URL
   - This may take some time depending on book size

## Health Checks

The deployed service includes a health check endpoint:
- `GET /health` - Returns service status and version

## Monitoring and Logs

### Railway Logs
- Access logs through the Railway dashboard
- Set up alerts for error conditions

### Performance Monitoring
- Monitor response times for the `/chat` endpoint
- Track usage statistics via the `/stats` endpoint

## Rollback Procedure

If issues occur after deployment:
1. Use Railway's version control to rollback to a previous working version
2. Ensure the previous version's environment variables are still valid
3. Test functionality after rollback

## Troubleshooting

### Common Issues

1. **API Keys Not Working**
   - Verify all API keys are correctly set in environment variables
   - Check for typos in key values

2. **CORS Errors**
   - Ensure `ALLOWED_ORIGINS` includes your frontend domain
   - Check that the domain includes both http and https if needed

3. **Database Connection Issues**
   - Verify Neon Postgres connection string is correct
   - Check that the database is accessible from the deployed environment

4. **Vector Database Issues**
   - Confirm Qdrant URL and API key are correct
   - Verify the collection exists and is properly configured

### Performance Issues
- Monitor response times
- Consider implementing caching for common queries
- Optimize chunk size and search parameters

## Scaling Considerations

- The application is designed to handle 100+ concurrent users
- Qdrant and Neon Postgres should scale automatically with usage
- Monitor costs as usage increases