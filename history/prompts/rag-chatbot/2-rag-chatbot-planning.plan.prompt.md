---
id: 2
title: "rag-chatbot-planning"
stage: "plan"
date: "2025-12-10"
surface: "agent"
model: "Claude Sonnet 4.5"
feature: "rag-chatbot"
branch: "1-rag-chatbot"
user: "user"
command: "/sp.plan"
labels: ["planning", "architecture", "rag", "ai", "docusaurus"]
links:
  spec: "specs/1-rag-chatbot/spec.md"
  ticket: null
  adr: null
  pr: null
files:
  - "specs/1-rag-chatbot/plan.md"
  - "specs/1-rag-chatbot/research.md"
  - "specs/1-rag-chatbot/data-model.md"
  - "specs/1-rag-chatbot/quickstart.md"
  - "specs/1-rag-chatbot/contracts/openapi.yaml"
tests: []
---

# RAG Chatbot Planning Work

## Prompt Text
```
project_overview:
  name: "RAG Chatbot for Physical AI Book"
  goal: "Build and deploy intelligent chatbot embedded in Docusaurus book"
  timeline: "1 day (8 hours)"
  methodology: "Spec-Kit Plus with Claude CLI - RAPID IMPLEMENTATION"

phases:
  phase_1_setup_and_ingestion:
    duration: "Hours 1-2 (2 hours)"
    deliverables:
      - "Project structure created"
      - "Dependencies installed"
      - "Book content ingested to Qdrant"
    tasks:
      - "Create chatbot/ folder with backend/, frontend/, scripts/"
      - "Create requirements.txt and install"
      - "Set up .env with API keys (Cohere, Qdrant, Neon, Google AI)"
      - "Create and run scripts/ingest.py (ingest all book content)"
      - "Verify Qdrant collection has 400+ chunks"
    validation:
      - "Qdrant collection populated"
      - "Test query returns results"

  phase_2_backend_api:
    duration: "Hours 3-4 (2 hours)"
    deliverables:
      - "FastAPI backend fully functional"
      - "/chat endpoint working"
      - "Postgres chat history storage"
    tasks:
      - "Create backend/main.py, rag.py, database.py, config.py"
      - "Implement RAG pipeline using Cohere embeddings + Qdrant"
      - "Chat generation via Gemini-2.5-flash"
      - "Implement /chat endpoint with selected text support"
      - "Add Neon Postgres integration"
      - "Add CORS middleware"
      - "Test with curl/Postman"
    validation:
      - "Can POST to /chat and get response"
      - "Chat saved to Postgres"

  phase_3_frontend_widget:
    duration: "Hours 5-6 (2 hours)"
    deliverables:
      - "React chat widget complete"
      - "Embedded in Docusaurus"
      - "End-to-end flow working"
    tasks:
      - "Create simple React widget (UMD/CDN)"
      - "Create ChatWidget.js with fetch to backend"
      - "Add selected text detection"
      - "Style widget (minimal)"
      - "Embed in Docusaurus src/theme/Root.js"
      - "Test locally"
    validation:
      - "Chat widget appears on book pages"
      - "Can ask questions and get answers"
      - "Selected text works"

  phase_4_deployment:
    duration: "Hours 7-8 (2 hours)"
    deliverables:
      - "Backend deployed to Railway"
      - "Docusaurus redeployed with chatbot"
      - "Production working"
    tasks:
      - "Deploy backend to Railway"
      - "Update CORS and frontend API URL"
      - "Rebuild and deploy Docusaurus"
      - "Test production"
      - "Create quick documentation"
    validation:
      - "Live chatbot works on deployed site"
      - "No production errors"

technical_decisions:
  decision_1_embedding_model:
    options:
      - "Cohere embed-english-v3.0 (FREE)"
      - "Cohere embed-multilingual-v3.0"
    chosen: "Cohere embed-english-v3.0"
    rationale: "0$ cost, high performance, works well with Qdrant"

  decision_2_chat_model:
    options:
      - "Gemini-2.5-flash (FREE, super fast)"
      - "Gemini-1.5-flash (fallback, FREE)"
    chosen: "Gemini-2.5-flash"
    rationale: "Fast, cheap, works perfectly for RAG"

  decision_3_deployment_platform:
    options:
      - "Railway (easy, $5 free credit)"
      - "Render"
      - "Vercel"
    chosen: "Railway"
    rationale: "Best balance of ease and performance"

  decision_4_frontend_framework:
    options:
      - "Pure React with Vite"
      - "CRA"
      - "Next.js"
    chosen: "Vite + React + TypeScript"
    rationale: "Fastest development UX"

  decision_5_chunk_strategy:
    options:
      - "Fixed 1000 chars"
      - "Sentence-aware chunking"
    chosen: "Sentence-aware chunking with overlap"
    rationale: "Best quality for RAG"

risk_mitigation:
  risk_1:
    description: "Google AI API limits reached"
    impact: "Medium"
    mitigation:
      - "Use gemini-1.5-flash as fallback"
      - "Add retry + caching"

  risk_2:
    description: "Qdrant free tier insufficient"
    impact: "Medium"
    mitigation:
      - "Monitor collection size"
      - "Optimize chunk sizes"

  risk_3:
    description: "Response times too slow (>10s)"
    impact: "Medium"
    mitigation:
      - "Gemini-2.5-flash for speed"
      - "Search top_k=3"

  risk_4:
    description: "Mobile selection issues"
    impact: "Low"
    mitigation:
      - "Fallback paste-text button"

success_metrics:
  must_achieve:
    - "Chatbot embedded on live site"
    - "Answers 80%+ accurately"
    - "Selected text works"
    - "Response < 5s"

  should_achieve:
    - "Response < 3s"
    - "Works on mobile"

  nice_to_achieve:
    - "Streaming responses"
    - "Dark mode"

documentation_plan:
  files_to_create:
    - "chatbot/README.md"
    - "chatbot/DEPLOYMENT.md"
    - "chatbot/API.md"
    - "chatbot/TROUBLESHOOTING.md"

file_structure_detailed:
  humanoid-robotics-book/:
    - "chatbot/"
      - "backend/"
      - "frontend/"
      - "scripts/"
      - "README.md"
      - "DEPLOYMENT.md"
      - "sp.specify"
      - "sp.plan"
      - "sp.tasks.md"
```

## Response Text
Completed the implementation plan for the RAG Chatbot feature, including:
- Filled technical context with Python 3.10+, TypeScript, FastAPI, React, Cohere, Qdrant, Gemini-2.5-flash
- Performed constitution check - all gates passed
- Created detailed project structure with backend, frontend, and Docusaurus integration
- Generated research.md with technology decisions and architecture research
- Created data-model.md with database schemas and API data models
- Created OpenAPI contract for the backend API
- Created quickstart.md with setup instructions
- Updated Claude agent context with new technologies

## Outcome
The implementation plan is complete with all required documentation artifacts. The plan includes research, data models, API contracts, and quickstart guide. The constitution check passed all compliance gates. The agent context was updated with the new technologies. Ready to proceed to task generation phase.