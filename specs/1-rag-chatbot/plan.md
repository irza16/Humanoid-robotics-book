# Implementation Plan: RAG Chatbot with Gemini via OpenAI SDK

**Branch**: `1-rag-chatbot` | **Date**: 2025-12-10 | **Spec**: [specs/1-rag-chatbot/spec.md](./spec.md)
**Version**: 2.0 | **Changelog**: v2.0: Use Gemini instead of OpenAI GPT | v1.0: Pure OpenAI
**Input**: Feature specification from `/specs/1-rag-chatbot/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a Retrieval-Augmented Generation (RAG) chatbot for the Physical AI & Humanoid Robotics book. The system will allow users to ask questions about book content and receive accurate answers with source attribution. The solution uses Cohere embeddings for semantic search in Qdrant vector database, Google Gemini 2.0 Flash via OpenAI SDK for cost-effective answer generation, and FastAPI for the backend API. A vanilla JavaScript chat widget will be embedded in the Docusaurus book site via theme customization, with special handling for user-selected text to provide enhanced context. The architecture separates concerns between backend processing and frontend presentation while ensuring minimal impact on page load times and supporting mobile responsiveness. This implementation fulfills the hackathon requirement to use OpenAI Agents SDK while leveraging the free tier of Gemini 2.0 Flash (1500 req/day).

## Technical Context

**Language/Version**: Python 3.10+ (backend), JavaScript (frontend)
**Primary Dependencies**: FastAPI, Cohere embeddings, Qdrant, OpenAI Agents SDK with Google Gemini 2.0 Flash, Docusaurus
**Storage**: Qdrant Cloud (vector storage), Neon Postgres (structured data), browser local storage (session)
**Testing**: pytest (backend), manual end-to-end testing
**Target Platform**: Web application (Docusaurus book site), cross-browser compatible
**Project Type**: Web application (backend API + frontend widget embedded in Docusaurus)
**Performance Goals**: <5s response time for chat queries, <200ms page load impact, support 100 concurrent users
**Constraints**: Must work within Docusaurus theme customization, mobile-responsive, secure API calls, fulfill OpenAI Agents SDK requirement for hackathon
**Scale/Scope**: Single book content (Physical AI & Humanoid Robotics), multiple concurrent users, chat history storage, cost-effective operation using free tier (1500 req/day)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Compliance Analysis

**Technical Accuracy First**: ✅ PASS
- Using official APIs: Cohere embeddings, Google AI (Gemini), Qdrant, FastAPI, React
- No hallucinated features; all technologies are industry-standard and publicly available

**Progressive Difficulty Structure**: ✅ PASS
- Feature builds on existing book content to provide enhanced learning experience
- Adds intelligent tutoring capability that supports the educational progression

**Real-World Applicability**: ✅ PASS
- Uses industry-standard RAG architecture with proven technologies
- Maps to real AI/ML workflows and semantic search patterns
- Deployable solution using cloud services (Railway, Qdrant Cloud, Neon)

**Consistent Terminology**: ✅ PASS
- RAG (Retrieval-Augmented Generation) is standard AI terminology
- Uses consistent language with the book content for AI/ML concepts

**Original Content with Manufacturer Specifications**: ✅ PASS
- Implementation uses official API specifications from technology providers
- No fabricated capabilities or features

**Setup-Ready Instructions**: ✅ PASS
- Plan includes clear deployment steps to Railway with environment configuration
- Will provide documentation for setup and troubleshooting

### Gate Status: ALL PASSED
Ready to proceed with Phase 0 research.

## Project Structure

### Documentation (this feature)

```text
specs/1-rag-chatbot/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (new chatbot directory)

```text
chatbot/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── rag.py               # RAG pipeline logic with OpenAI Agents SDK and Gemini
│   ├── database.py          # Neon Postgres connection
│   ├── config.py            # Configuration and settings (loads GEMINI_API_KEY)
│   ├── requirements.txt     # Python dependencies
│   └── .env.example         # Environment variables template
├── frontend/
│   └── static/
│       └── chatbot-widget.js # Vanilla JavaScript chat widget
├── scripts/
│   └── ingest.py            # Data ingestion script
├── README.md
├── DEPLOYMENT.md
└── API.md
```

### Integration with Existing Docusaurus

```text
src/
└── theme/
    └── Root.js              # Docusaurus theme customization to embed chat widget

chatbot/                     # New directory for RAG chatbot
└── [as shown above]
```

**Structure Decision**: Web application with separate backend (FastAPI) and frontend (JavaScript widget) components, integrated into existing Docusaurus book through theme customization. This follows the "Web application" pattern from the template with clear separation of concerns between backend API and frontend widget.

## Implementation Phases

### Phase 0: Setup & Ingestion (Hours 1-2)
**Duration**: Hours 1-2

**Tasks**:
- Create chatbot/backend/, chatbot/frontend/, chatbot/scripts/
- Create requirements.txt (agents SDK, fastapi, qdrant, cohere, neon)
- Create .env with: GEMINI_API_KEY, QDRANT_URL/KEY, NEON_URL, COHERE_KEY
- Create scripts/ingest.py (sitemap → Cohere embeddings → Qdrant)
- Run ingestion: python scripts/ingest.py

**Deliverables**:
- Qdrant collection 'book_content' with 400+ chunks
- Test query works

**Validation**: qdrant.query_points returns results

### Phase 1: Backend API (Hours 3-4)
**Duration**: Hours 3-4

**Tasks**:
- Create backend/config.py (load GEMINI_API_KEY)
- Create backend/database.py (Neon Postgres schema + functions)
- Create backend/rag.py with Gemini provider:
  - AsyncOpenAI(base_url='https://generativelanguage.googleapis.com/v1beta/openai/')
  - OpenAIChatCompletionsModel(model='gemini-2.0-flash-exp')
  - Agent with @function_tool retrieve()
- Create backend/main.py (FastAPI + /chat endpoint)
- Add CORS for https://irza16.github.io
- Test: curl -X POST /chat -d '{"question":"What is ROS 2?"}'

**Deliverables**:
- FastAPI running on localhost:8000
- /chat returns answers with sources
- Chat saved to Postgres

**Validation**: API responds correctly, history saved

### Phase 2: Frontend Integration (Hours 5-6)
**Duration**: Hours 5-6

**Tasks**:
- Create static/chatbot-widget.js (vanilla JS):
  - Floating button
  - Modal chat window
  - fetch() to backend /chat
  - window.getSelection() for selected text
- Create src/theme/Root.js in Docusaurus
- Load chatbot-widget.js script
- Test locally: npm start
- Test selected text → question flow

**Deliverables**:
- Chat widget on all book pages
- Questions get answered
- Selected text works

**Validation**: End-to-end chat works locally

### Phase 3: Deployment (Hours 7-8)
**Duration**: Hours 7-8

**Tasks**:
- Deploy backend to Railway: railway up
- Set Railway env vars (GEMINI_API_KEY, QDRANT, NEON, COHERE)
- Update chatbot-widget.js with Railway URL
- Build Docusaurus: npm run build
- Deploy: set GIT_USER=irza16 && npm run deploy
- Test production
- Write quick README.md

**Deliverables**:
- Backend live on Railway
- Chatbot working on https://irza16.github.io/Humanoid-robotics-book/
- Documentation complete

**Validation**: Production chatbot works, no errors

## Technical Decisions

### LLM Choice
**Chosen**: Gemini 2.0 Flash via OpenAI SDK
**Reason**: FREE (1500/day), fulfills OpenAI SDK requirement, fast

### Embeddings
**Chosen**: Cohere embed-english-v3.0
**Reason**: Already working and proven effective for semantic search

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
