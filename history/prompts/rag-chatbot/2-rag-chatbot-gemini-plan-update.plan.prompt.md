---
id: 2-rag-chatbot-gemini-plan-update
title: "RAG Chatbot Gemini Plan Update"
stage: "plan"
date: "2025-12-10"
model: "Claude Sonnet 4.5"
feature: "rag-chatbot"
branch: "1-rag-chatbot"
user: "user"
command: "/sp.plan.v2"
labels: ["planning", "rag-chatbot", "gemini", "migration"]
links:
  plan: "specs/1-rag-chatbot/plan.md"
  spec: "specs/1-rag-chatbot/spec.md"
files:
  - "specs/1-rag-chatbot/plan.md"
tests: []
---

# RAG Chatbot Gemini Plan Update

## Prompt

```
/sp.plan.v2
project: "RAG Chatbot with Gemini via OpenAI SDK"
timeline: "1 day (8 hours)"
version: "2.0"
changelog: "v2.0: Use Gemini instead of OpenAI GPT | v1.0: Pure OpenAI"

phases:
  phase_1_setup_ingestion:
    duration: "Hours 1-2"
    tasks:
      - "Create chatbot/backend/, chatbot/frontend/, chatbot/scripts/"
      - "Create requirements.txt (agents SDK, fastapi, qdrant, cohere, neon)"
      - "Create .env with: GEMINI_API_KEY, QDRANT_URL/KEY, NEON_URL, COHERE_KEY"
      - "Create scripts/ingest.py (sitemap → Cohere embeddings → Qdrant)"
      - "Run ingestion: python scripts/ingest.py"
    deliverables:
      - "Qdrant collection 'book_content' with 400+ chunks"
      - "Test query works"
    validation: "qdrant.query_points returns results"

  phase_2_backend_api:
    duration: "Hours 3-4"
    tasks:
      - "Create backend/config.py (load GEMINI_API_KEY)"
      - "Create backend/database.py (Neon Postgres schema + functions)"
      - "Create backend/rag.py with Gemini provider:"
      - "  - AsyncOpenAI(base_url='https://generativelanguage.googleapis.com/v1beta/openai/')"
      - "  - OpenAIChatCompletionsModel(model='gemini-2.0-flash-exp')"
      - "  - Agent with @function_tool retrieve()"
      - "Create backend/main.py (FastAPI + /chat endpoint)"
      - "Add CORS for https://irza16.github.io"
      - "Test: curl -X POST /chat -d '{\"question\":\"What is ROS 2?\"}'"
    deliverables:
      - "FastAPI running on localhost:8000"
      - "/chat returns answers with sources"
      - "Chat saved to Postgres"
    validation: "API responds correctly, history saved"

  phase_3_frontend_integration:
    duration: "Hours 5-6"
    tasks:
      - "Create static/chatbot-widget.js (vanilla JS):"
      - "  - Floating button"
      - "  - Modal chat window"
      - "  - fetch() to backend /chat"
      - "  - window.getSelection() for selected text"
      - "Create src/theme/Root.js in Docusaurus"
      - "Load chatbot-widget.js script"
      - "Test locally: npm start"
      - "Test selected text → question flow"
    deliverables:
      - "Chat widget on all book pages"
      - "Questions get answered"
      - "Selected text works"
    validation: "End-to-end chat works locally"

  phase_4_deployment:
    duration: "Hours 7-8"
    tasks:
      - "Deploy backend to Railway: railway up"
      - "Set Railway env vars (GEMINI_API_KEY, QDRANT, NEON, COHERE)"
      - "Update chatbot-widget.js with Railway URL"
      - "Build Docusaurus: npm run build"
      - "Deploy: set GIT_USER=irza16 && npm run deploy"
      - "Test production"
      - "Write quick README.md"
    deliverables:
      - "Backend live on Railway"
      - "Chatbot working on https://irza16.github.io/Humanoid-robotics-book/"
      - "Documentation complete"
    validation: "Production chatbot works, no errors"

technical_decisions:
  llm_choice:
    chosen: "Gemini 2.0 Flash via OpenAI SDK"
    reason: "FREE (1500/day), fulfills OpenAI SDK requirement, fast"

  embeddings:
    chosen: "Cohere embed-english-v3.0"
    reason: "Already working
```

## Response

Updated the existing RAG chatbot implementation plan to reflect the migration from OpenAI to Gemini 2.0 Flash via OpenAI SDK. The changes include:

- Updated title and metadata to reflect v2.0 with Gemini implementation
- Updated technical context to reflect new dependencies (OpenAI Agents SDK with Google Gemini 2.0 Flash) and JavaScript instead of TypeScript
- Updated project structure to reflect vanilla JavaScript chat widget instead of React
- Added detailed implementation phases with 8-hour timeline:
  - Phase 0: Setup & Ingestion (Hours 1-2)
  - Phase 1: Backend API (Hours 3-4)
  - Phase 2: Frontend Integration (Hours 5-6)
  - Phase 3: Deployment (Hours 7-8)
- Added technical decisions section for LLM choice and embeddings
- Maintained all constitutional compliance checks

The plan now properly reflects the cost-effective migration to Gemini 2.0 Flash while maintaining the same RAG functionality using Cohere embeddings and Qdrant vector database, and fulfilling the hackathon requirement to use OpenAI Agents SDK.

## Outcome

The RAG chatbot implementation plan has been successfully updated to reflect the Gemini 2.0 Flash implementation via OpenAI SDK, enabling a clear 8-hour implementation timeline with cost-effective AI responses (1500 free requests/day) while maintaining the same functionality. The plan is ready for the task generation phase.

## Evaluation

The plan update successfully addresses the migration requirement while maintaining all implementation structure. The cost savings are significant (moving from $5-10/month to free tier), and the technical approach leverages the OpenAI Agents SDK as required for the hackathon. The 8-hour timeline provides a realistic and achievable implementation schedule.