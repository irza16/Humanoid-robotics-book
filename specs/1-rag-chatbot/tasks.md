# Implementation Tasks: RAG Chatbot with Gemini via OpenAI SDK

**Feature**: RAG Chatbot with Gemini via OpenAI SDK
**Branch**: `1-rag-chatbot`
**Version**: 2.0
**Changelog**: v2.0: Use Gemini instead of OpenAI GPT | v1.0: Pure OpenAI
**Spec**: [specs/1-rag-chatbot/spec.md](specs/1-rag-chatbot/spec.md)
**Plan**: [specs/1-rag-chatbot/plan.md](specs/1-rag-chatbot/plan.md)

## Implementation Strategy

This implementation follows a phased approach with user stories organized by priority (P1, P2, P3). Each phase builds upon the previous one, with Phase 1 (Setup) and Phase 2 (Foundational) providing the necessary infrastructure for the user-facing features. The MVP scope includes User Story 1 (core chat functionality) to deliver immediate value.

## Dependencies

- User Story 1 (P1) must be completed before User Story 2 (P2) and User Story 3 (P3)
- User Story 2 (P2) can be developed in parallel with User Story 3 (P3) after User Story 1 completion
- All user stories depend on completion of Setup and Foundational phases

## Parallel Execution Examples

Per User Story:
- **US1**: Tasks T021-P through T028 can be developed in parallel (different components: API endpoint, RAG logic, UI, API client)
- **US2**: Tasks T031-P through T035 can be developed in parallel (frontend detection, API updates, RAG pipeline, UI indicators)
- **US3**: Tasks T037-P through T041 can be developed in parallel (session management, database, UI, attribution display)

## Task Dependencies

- **Setup Phase**: No dependencies (can start immediately)
- **Foundational Phase**: Depends on T001-T006 (basic structure must exist)
- **US1**: Depends on foundational tasks T011-T020 (infrastructure must be ready)
- **US2**: Depends on US1 tasks T021-T030 (core chat functionality required)
- **US3**: Depends on US1 tasks T021-T030 (core chat functionality required)
- **Polish Phase**: Depends on all user story completion

## Phase 1: Setup (Project Initialization)

**Goal**: Initialize project structure and dependencies for the RAG chatbot

- [X] T001 Create chatbot/ directory structure with backend/, frontend/static/, scripts/ subdirectories
- [X] T002 [P] Create backend/requirements.txt with FastAPI, agents, cohere, qdrant-client, psycopg2-binary, python-dotenv, pydantic, pydantic-settings
- [X] T003 [P] Create frontend/static/chatbot-widget.js with basic JavaScript structure
- [X] T004 [P] Create .env.example with GEMINI_API_KEY, COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY, NEON_DATABASE_URL, SECRET_KEY, ALLOWED_ORIGINS
- [X] T005 Create backend/main.py with basic FastAPI app structure
- [X] T006 Create src/theme/Root.js for Docusaurus integration
- [X] T007 Create scripts/ingest.py with basic script structure for content ingestion
- [X] T008 Create chatbot/README.md with project overview and setup instructions
- [X] T009 Create chatbot/DEPLOYMENT.md with deployment instructions
- [X] T010 Create chatbot/API.md with API documentation reference

## Phase 2: Foundational (Blocking Prerequisites)

**Goal**: Implement core infrastructure components needed by all user stories

- [X] T011 [P] Implement config.py with settings model using pydantic-settings for backend configuration (load GEMINI_API_KEY)
- [X] T012 [P] Implement database.py with Neon Postgres connection and chat session/message models
- [X] T013 [P] Implement rag.py with basic RAG pipeline structure using OpenAI Agents SDK and Gemini 2.0 Flash:
  - AsyncOpenAI with base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
  - OpenAIChatCompletionsModel with model='gemini-2.0-flash-exp'
  - Agent with @function_tool for retrieval
- [X] T014 [P] Setup CORS middleware in main.py to allow Docusaurus domain access (https://irza16.github.io)
- [X] T015 [P] Create chat_sessions table schema in Neon Postgres with id, user_id, created_at columns
- [X] T016 [P] Create chat_messages table schema in Neon Postgres with id, session_id, question, answer, selected_text, sources, created_at columns
- [X] T017 [P] Implement Qdrant collection setup for book_content with proper vector configuration (1024 dimensions, cosine distance)
- [X] T018 [P] Implement basic health check endpoint GET /health in main.py
- [X] T019 [P] Implement input validation for question length (1-2000 chars) and selected text (0-5000 chars)
- [X] T020 [P] Implement basic error handling and logging middleware

## Phase 3: User Story 1 - Ask Questions About Book Content (Priority: P1)

**Goal**: Enable users to ask questions about book content and receive answers with source attribution

**Independent Test Criteria**: User can open chat widget, ask a question about book content, and receive an accurate answer with source citations

- [X] T021 [P] [US1] Implement POST /chat endpoint to handle question requests without selected text
- [X] T022 [P] [US1] Implement Cohere embedding generation for user questions using embed-english-v3.0
- [X] T023 [P] [US1] Implement Qdrant search to retrieve top 3-5 relevant book content chunks
- [X] T024 [P] [US1] Implement OpenAI Agents SDK with Gemini 2.0 Flash integration for answer generation:
  - Use Runner.run_sync(agent, input=question) pattern
  - Agent with instructions to call retrieve(query) first
  - Answer using ONLY retrieved content
- [X] T025 [P] [US1] Implement source attribution in responses with URL, title, and content excerpt
- [X] T026 [P] [US1] Create chatbot-widget.js UI with floating button, modal window, message display and input field
- [X] T027 [P] [US1] Implement fetch() API client in frontend to communicate with backend /chat endpoint
- [X] T028 [P] [US1] Implement basic chat message display with loading states in vanilla JavaScript
- [X] T029 [P] [US1] Test end-to-end flow: question → API → RAG → answer with sources
- [X] T030 [US1] Handle case where question is not covered in book content with appropriate response

## Phase 4: User Story 2 - Ask Questions About Selected Text (Priority: P2)

**Goal**: Enable users to select text in the book and ask questions about that specific content

**Independent Test Criteria**: User can select text on a book page, ask a question about it, and receive a response focused on the selected content with additional context

- [X] T031 [P] [US2] Implement selected text detection using window.getSelection() API in chatbot-widget.js
- [X] T032 [P] [US2] Modify POST /chat endpoint to accept and prioritize selected_text in context
- [X] T033 [P] [US2] Update RAG pipeline to boost relevance for content matching selected text
- [X] T034 [P] [US2] Implement visual indicator in UI when selected text is detected
- [X] T035 [P] [US2] Add selected text context to Gemini prompt for focused responses
- [X] T036 [P] [US2] Test end-to-end flow: select text → ask question → focused answer with additional context

## Phase 5: User Story 3 - View Chat History and Source Attribution (Priority: P3)

**Goal**: Enable users to review conversation history and see source attribution for answers

**Independent Test Criteria**: User can see previous questions and answers with proper source citations and understand which book sections were used

- [X] T037 [P] [US3] Implement session management to link messages to chat sessions
- [X] T038 [P] [US3] Implement database storage and retrieval for chat history
- [X] T039 [P] [US3] Update chatbot-widget.js UI to display conversation history
- [X] T040 [P] [US3] Implement source attribution display with clickable links to book sections
- [X] T041 [P] [US3] Add session persistence across page refreshes
- [X] T042 [P] [US3] Test end-to-end flow: multiple questions → history display → source verification

## Phase 6: Polish & Cross-Cutting Concerns

**Goal**: Add finishing touches, security measures, and performance optimizations

- [X] T043 [P] Implement rate limiting middleware (max 10 requests per minute per IP)
- [X] T044 [P] Implement input sanitization to prevent injection attacks
- [X] T045 [P] Add response time monitoring and logging
- [X] T046 [P] Implement retry logic with exponential backoff for API calls
- [X] T047 [P] Optimize frontend JavaScript loading performance
- [X] T048 [P] Add mobile-responsive design for chat widget
- [X] T049 [P] Implement POST /ingest endpoint for book content ingestion
- [X] T050 [P] Create sitemap.xml parser to extract all book page URLs
- [X] T051 [P] Implement sentence-aware text chunking with overlap for ingestion
- [X] T052 [P] Add POST /stats endpoint for usage analytics
- [X] T053 [P] Integrate chat widget into Docusaurus via src/theme/Root.js customization
- [X] T054 [P] Add comprehensive error handling and user-friendly error messages
- [X] T055 [P] Write API tests for all endpoints using pytest
- [X] T056 [P] Write frontend JavaScript tests
- [X] T057 [P] Performance test: verify response time < 5s for 95% of requests
- [X] T058 [P] Security review: validate all inputs, check for vulnerabilities
- [X] T059 [P] Documentation: update README.md with complete usage instructions
- [X] T060 [P] Deployment: prepare for Railway deployment with proper environment configuration