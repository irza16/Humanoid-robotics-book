# Research Findings: Claude Code Subagents & Reusable Agent Skills

## Decision: Qdrant Collection Structure
**Rationale**: Based on the specification, we need to query module-specific collections in Qdrant. The collections should be named with a consistent pattern that includes the module identifier.
**Implementation**: Collections will be named as `book_content_module-1-ros2`, `book_content_module-2-simulation`, `book_content_module-3-isaac`, and `book_content_module-4-vla`. The system will have a fallback to the general `book_content` collection if module-specific collections don't exist.

## Decision: Performance Optimization for Routing
**Rationale**: The routing logic must add minimal latency (<100ms) to maintain overall response times under 5 seconds.
**Implementation**: Routing will use a pre-built keyword mapping dictionary with O(1) lookup time. The keyword matching will be simple string operations to ensure fast execution.

## Decision: Backward Compatibility Strategy
**Rationale**: The existing API and functionality must continue to work without changes for current users.
**Implementation**: The RAGPipeline class will be extended to support both the new routing functionality and the original pipeline. A parameter will control which approach to use, defaulting to the new routing for new code but maintaining the original for compatibility.

## Decision: Agent Architecture Pattern
**Rationale**: Agents need to be modular and reusable while maintaining consistency in their interface.
**Implementation**: All agents will inherit from a base Agent class that defines the common interface. Each agent will have its own specialized instructions and will use the shared agent skills.

## Decision: Error Handling and Fallback
**Rationale**: The system must be resilient to failures in routing or subagent functionality.
**Implementation**: Each component will have comprehensive error handling with fallbacks to the original pipeline. If routing fails, the system will default to the ROS2Agent as specified in the requirements.

## Decision: Response Format Consistency
**Rationale**: The API response format must remain unchanged to maintain compatibility with existing clients.
**Implementation**: The response model will be extended to optionally include a `subagent_used` field for transparency, but this will be optional and not break existing clients.

## Alternatives Considered

### Alternative 1: Full Replacement vs. Backward Compatible
- **Considered**: Completely replacing the original RAG pipeline
- **Rejected**: Would break existing functionality and require client-side changes
- **Chosen**: Extending the existing pipeline with optional routing functionality

### Alternative 2: Complex ML-Based Routing vs. Keyword-Based Routing
- **Considered**: Using machine learning models to classify questions
- **Rejected**: Would add significant latency and complexity
- **Chosen**: Simple keyword matching for fast, deterministic routing

### Alternative 3: Separate Service vs. Integrated Approach
- **Considered**: Creating a separate microservice for agent routing
- **Rejected**: Would add network latency and operational complexity
- **Chosen**: Integrated approach within existing backend service