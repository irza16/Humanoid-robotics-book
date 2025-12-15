# Feature Specification: RAG Chatbot with Gemini via OpenAI SDK

**Feature Branch**: `1-rag-chatbot`
**Created**: 2025-12-10
**Version**: 2.0
**Changelog**: v2.0: Use Gemini 2.0 Flash via OpenAI SDK (free) | v1.0: Pure OpenAI
**Status**: Draft
**Input**: User description: "Build and embed a Retrieval-Augmented Generation (RAG) chatbot within the published Docusaurus book. The chatbot will answer user questions about the book's content using semantic search and AI generation. It must support both general queries and questions about user-selected text snippets. Updated to use OpenAI Agents SDK with Gemini 2.0 Flash (free tier) via OpenAI SDK."

## LLM Implementation Change

**Requirement**: OpenAI Agents SDK (hackathon mandatory)
**Actual Model**: Gemini 2.0 Flash (FREE)

## Environment Variables

**Add**: ["GEMINI_API_KEY"]
**Remove**: ["OPENAI_API_KEY"]
**Keep**: ["QDRANT_URL", "QDRANT_API_KEY", "NEON_DATABASE_URL", "COHERE_API_KEY"]

## System Architecture

The system will use the OpenAI Agents SDK to interface with the Gemini 2.0 Flash model through an OpenAI-compatible API. The RAG system will continue to use Cohere embeddings and Qdrant vector database for content retrieval.

## Cost Benefits

- Before: OpenAI GPT: $5-10/month
- After: Gemini: FREE (1500 req/day)

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ask Questions About Book Content (Priority: P1)

A student reading the Physical AI & Humanoid Robotics book wants to ask questions about the content to better understand complex topics. The user types a question into the chat widget embedded in the Docusaurus site and receives an accurate answer based on the book's content with proper source attribution.

**Why this priority**: This is the core functionality that delivers immediate value to users by providing an AI-powered tutor that can answer questions about the book content, enhancing the learning experience.

**Independent Test**: Can be fully tested by asking various questions about the book content and verifying that the chatbot provides accurate answers with source citations, delivering immediate educational value.

**Acceptance Scenarios**:

1. **Given** user is viewing any page of the Physical AI book, **When** user opens the chat widget and asks a question about book content, **Then** user receives an accurate answer based on the book content with source citations
2. **Given** user asks a question not covered in the book, **When** user submits the question, **Then** user receives a response indicating the information is not available in the book

---

### User Story 2 - Ask Questions About Selected Text (Priority: P2)

A student highlights specific text in the book and wants clarification about that particular content. The user selects text, asks a question about it, and receives an answer focused on the selected content with additional context from related book sections.

**Why this priority**: This enhances the learning experience by allowing users to get immediate clarification on specific passages they find confusing, making the learning process more interactive and personalized.

**Independent Test**: Can be fully tested by selecting text in the book, asking a question about it, and verifying that the response is focused on the selected text while incorporating related content from the book.

**Acceptance Scenarios**:

1. **Given** user has selected text on a book page, **When** user asks a question about the selected text, **Then** user receives an answer focused on the selected content with additional relevant context
2. **Given** user has selected text and asked a related question, **When** user submits the question, **Then** response includes proper source attribution for all referenced content

---

### User Story 3 - View Chat History and Source Attribution (Priority: P3)

A student wants to review previous conversations and understand which parts of the book were used to generate answers. The system stores conversation history and clearly shows which book sections were used to answer each question.

**Why this priority**: This provides transparency and allows students to follow up on previous questions while understanding the source of information, building trust in the AI system.

**Independent Test**: Can be tested by engaging in a conversation, asking follow-up questions, and verifying that source attribution is clear and conversation history is properly maintained.

**Acceptance Scenarios**:

1. **Given** user has asked multiple questions, **When** user views the conversation, **Then** all previous questions and answers are displayed with proper source attribution
2. **Given** user receives an answer, **When** user reviews the response, **Then** clear source citations indicate which book sections were used to generate the answer

---

### Edge Cases

- What happens when the AI cannot find relevant content in the book to answer a question?
- How does the system handle very long selected text (e.g., entire paragraphs)?
- How does the system handle questions that span multiple unrelated topics in the book?
- What happens when the backend API is temporarily unavailable?
- How does the system handle extremely long questions or answers?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to ask questions about the Physical AI book content through an embedded chat widget
- **FR-002**: System MUST provide accurate answers based on the book's content using semantic search and AI generation via OpenAI Agents SDK with Gemini 2.0 Flash
- **FR-003**: System MUST support questions about user-selected text with enhanced context
- **FR-004**: System MUST provide clear source attribution for all answers with links to relevant book sections
- **FR-005**: System MUST store conversation history for analytics and user reference
- **FR-006**: System MUST integrate seamlessly with the Docusaurus book site without affecting performance
- **FR-007**: System MUST handle concurrent users efficiently with acceptable response times
- **FR-008**: System MUST sanitize all user inputs to prevent injection attacks
- **FR-009**: System MUST work across different browsers and devices (responsive design)
- **FR-010**: System MUST maintain user privacy and not store personal information unnecessarily
- **FR-011**: System MUST use OpenAI Agents SDK with Gemini 2.0 Flash via OpenAI SDK for cost-effective AI responses
- **FR-012**: System MUST implement function tools for RAG retrieval using Cohere embeddings and Qdrant vector database

### Key Entities

- **Chat Session**: Represents a user's conversation with the chatbot, containing metadata about the interaction
- **Chat Message**: Individual question-answer pairs within a session, including the original question, AI response, selected text context, and source citations
- **Book Content**: The source material from the Physical AI book that is indexed for semantic search, including text chunks with metadata (URL, page title, chunk index)
- **User Query**: The question input from the user, potentially including selected text context for enhanced responses

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can ask questions and receive relevant answers within 5 seconds response time
- **SC-002**: 90% of user questions about book content receive accurate answers based on relevant book sections
- **SC-003**: 80% of users who use the chatbot find it helpful for understanding book content
- **SC-004**: The system successfully handles 100 concurrent users without performance degradation
- **SC-005**: All answers include proper source attribution with specific references to book sections
- **SC-006**: The chat widget integrates seamlessly without negatively impacting page load times (under 200ms additional load time)
- **SC-007**: 95% of user-selected text questions receive contextually appropriate responses
- **SC-008**: The system operates cost-effectively using Gemini 2.0 Flash with 1500 free requests per day instead of paid OpenAI services
- **SC-009**: The OpenAI Agents SDK integration successfully processes user queries through the Gemini 2.0 Flash model
- **SC-010**: The RAG system achieves 95% accuracy in retrieving relevant book content for user queries