---
id: 1-rag-chatbot-gemini-spec-update
title: "RAG Chatbot Gemini Spec Update"
stage: "spec"
date: "2025-12-10"
model: "Claude Sonnet 4.5"
feature: "rag-chatbot"
branch: "1-rag-chatbot"
user: "user"
command: "/sp.specify.v2"
labels: ["specification", "rag-chatbot", "gemini", "migration"]
links:
  spec: "specs/1-rag-chatbot/spec.md"
  checklist: "specs/1-rag-chatbot/checklists/requirements.md"
files:
  - "specs/1-rag-chatbot/spec.md"
  - "specs/1-rag-chatbot/checklists/requirements.md"
tests: []
---

# RAG Chatbot Gemini Spec Update

## Prompt

```
/sp.specify.v2
title: "RAG Chatbot with Gemini via OpenAI SDK"
version: "2.0"
changelog: "v2.0: Use Gemini 2.0 Flash via OpenAI SDK (free) | v1.0: Pure OpenAI"

llm_change:
  requirement: "OpenAI Agents SDK (hackathon mandatory)"
  actual_model: "Gemini 2.0 Flash (FREE)"

  implementation: |
    ```python
    from agents import OpenAIChatCompletionsModel, AsyncOpenAI

    provider = AsyncOpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash-exp",
        openai_client=provider
    )
    ```

environment_variables:
  add: ["GEMINI_API_KEY"]
  remove: ["OPENAI_API_KEY"]
  keep: ["QDRANT_URL", "QDRANT_API_KEY", "NEON_DATABASE_URL", "COHERE_API_KEY"]

files_to_update:
  backend/rag.py: "Use Gemini provider pattern above"
  backend/config.py: "Load GEMINI_API_KEY instead of OPENAI_API_KEY"
  .env: "Add GEMINI_API_KEY, remove OPENAI_API_KEY"

complete_rag_example: |
  ```python
  import os
  from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool
  from qdrant_client import QdrantClient
  import cohere

  # Gemini via OpenAI SDK
  provider = AsyncOpenAI(
      api_key=os.getenv("GEMINI_API_KEY"),
      base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
  )

  model = OpenAIChatCompletionsModel(
      model="gemini-2.0-flash-exp",
      openai_client=provider
  )

  # Cohere embeddings
  cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))
  qdrant = QdrantClient(url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY"))

  @function_tool
  def retrieve(query: str) -> list[str]:
      embedding = cohere_client.embed(
          model="embed-english-v3.0",
          input_type="search_query",
          texts=[query]
      ).embeddings[0]

      results = qdrant.query_points(
          collection_name="book_content",
          query=embedding,
          limit=3
      )
      return [p.payload["text"] for p in results.points]

  agent = Agent(
      name="BookTutor",
      instructions="You are a tutor. Call retrieve(query) first. Answer using ONLY retrieved content.",
      model=model,
      tools=[retrieve]
  )

  # In FastAPI: result = Runner.run_sync(agent, input=question)
  ```

unchanged:
  - "FastAPI backend"
  - "Qdrant vector DB"
  - "Neon Postgres"
  - "Frontend widget"
  - "Deployment (Railway)"
  - "Cohere embeddings"

cost_savings:
  before: "OpenAI GPT: $5-10/month"
  after: "Gemini: FREE (1500 req/day)"

migration_steps:
  - "Get key: https://aistudio.google.com/apikey"
  - "Update .env: GEMINI_API_KEY=..."
  - "Update rag.py with Gemini provider"
  - "Update config.py to load GEMINI_API_KEY"
  - "Test locally"
  - "Update Railway env vars"

end_of_spec
```

## Response

Updated the existing RAG chatbot specification to reflect the migration from OpenAI to Gemini 2.0 Flash via OpenAI SDK. The changes include:

- Updated title and version information to reflect v2.0 with Gemini implementation
- Added LLM Implementation Change section with requirement and model details
- Updated environment variables to use GEMINI_API_KEY instead of OPENAI_API_KEY
- Added System Architecture section describing the OpenAI Agents SDK integration
- Updated functional requirements to include FR-011 and FR-012 for the new implementation
- Updated success criteria to include cost benefits and technical outcomes
- Updated the quality checklist to match the new specification title
- Removed specific code implementation details to maintain specification abstraction

The specification now properly reflects the cost-effective migration to Gemini 2.0 Flash while maintaining the same RAG functionality using Cohere embeddings and Qdrant vector database.

## Outcome

The RAG chatbot specification has been successfully updated to reflect the Gemini 2.0 Flash implementation via OpenAI SDK, enabling cost-effective AI responses (1500 free requests/day) while maintaining the same functionality. The specification is ready for the planning phase.

## Evaluation

The specification update successfully addresses the migration requirement while maintaining all user-facing functionality. The cost savings are significant (moving from $5-10/month to free tier), and the technical approach leverages the OpenAI Agents SDK as required for the hackathon.