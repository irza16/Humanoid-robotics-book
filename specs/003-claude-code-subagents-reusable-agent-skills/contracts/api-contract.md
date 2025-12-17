# API Contract: Multi-Agent RAG System

## Overview
This document defines the API contracts for the multi-agent RAG system with specialized subagents and reusable agent skills.

## Base API (Unchanged)
The existing API endpoints remain unchanged to maintain backward compatibility.

### Chat Endpoint
```
POST /chat
Content-Type: application/json

Request:
{
  "question": "string, required",
  "selected_text": "string, optional",
  "session_id": "string, optional"
}

Response:
{
  "answer": "string",
  "sources": [
    {
      "url": "string",
      "title": "string",
      "content": "string"
    }
  ],
  "session_id": "string",
  "subagent_used": "string, optional - indicates which subagent processed the request"
}
```

## Internal API Contracts

### Agent Skills Interface
```
search_module_content(module_name: str, query: str) -> List[str]
```
- **Purpose**: Search specific module content in Qdrant
- **Parameters**:
  - module_name: Name of the module collection to search
  - query: Search query string
- **Returns**: List of relevant text chunks
- **Error handling**: Returns empty list on failure

```
find_code_examples(topic: str, language: Optional[str] = None) -> List[str]
```
- **Purpose**: Find code snippets related to a topic
- **Parameters**:
  - topic: Topic to search for code examples
  - language: Optional language filter
- **Returns**: List of code example text chunks
- **Error handling**: Returns empty list on failure

```
get_prerequisites(topic: str) -> str
```
- **Purpose**: Get prerequisite knowledge for a topic
- **Parameters**:
  - topic: Topic to get prerequisites for
- **Returns**: Prerequisite information as string
- **Error handling**: Returns general recommendation on failure

```
explain_concept(concept: str) -> str
```
- **Purpose**: Get detailed explanation of a core concept
- **Parameters**:
  - concept: Concept to explain
- **Returns**: Detailed explanation as string
- **Error handling**: Returns unable-to-explain message on failure

### Agent Interface
```
process_query(question: str, selected_text: Optional[str] = None) -> Tuple[str, List[Dict]]
```
- **Purpose**: Process a query through the agent
- **Parameters**:
  - question: User question to answer
  - selected_text: Optional selected text to focus on
- **Returns**: Tuple of (answer string, sources list)
- **Error handling**: Returns error message as answer

### Routing Interface
```
route_to_subagent(question: str) -> Agent
```
- **Purpose**: Route a question to the appropriate subagent
- **Parameters**:
  - question: Question string to route
- **Returns**: Appropriate Agent instance
- **Error handling**: Returns default ROS2Agent on failure

## Performance Contracts
- Routing decision time: <100ms
- Total response time: <5s
- Module-specific search performance: Comparable to general search
- Error fallback time: Should not exceed normal processing time significantly

## Error Handling Contracts
- All agent skills must handle exceptions gracefully
- Fallback to general RAG pipeline if subagent routing fails
- Maintain existing error response format
- Log routing and processing errors for monitoring

## Backward Compatibility Contracts
- Response format remains unchanged except for optional subagent_used field
- All existing API endpoints continue to function
- Existing client code should continue to work without modifications
- Optional parameter to disable new routing functionality (future enhancement)