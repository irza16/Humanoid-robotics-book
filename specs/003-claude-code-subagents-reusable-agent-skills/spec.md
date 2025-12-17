# Claude Code Subagents & Reusable Agent Skills

## Feature Overview

**Title**: Claude Code Subagents & Reusable Agent Skills
**Version**: 1.0
**Purpose**: Earn 50 bonus points by implementing multi-agent architecture with reusable intelligence

Enhance the RAG chatbot with specialized subagents for each course module and reusable agent skills. This demonstrates advanced AI architecture with domain-specific expertise and intelligent question routing.

## User Scenarios & Testing

### Primary User Scenarios
1. As a student, I want to ask ROS 2 related questions and get responses from a specialized ROS 2 expert agent
2. As a student, I want to ask simulation-related questions and get responses from a specialized simulation expert agent
3. As a student, I want to ask Isaac-related questions and get responses from a specialized Isaac expert agent
4. As a student, I want to ask VLA-related questions and get responses from a specialized VLA expert agent
5. As a student, I want my questions to be automatically routed to the most appropriate specialized agent
6. As a developer, I want to use reusable agent skills across different specialized agents

### Testing Scenarios
- Test routing of ROS 2 questions to ROS 2 agent
- Test routing of simulation questions to simulation agent
- Test routing of Isaac questions to Isaac agent
- Test routing of VLA questions to VLA agent
- Test fallback routing when no keywords match
- Test functionality of each reusable agent skill
- Test backward compatibility with existing API

## Functional Requirements

### FR1: Reusable Agent Skills
- The system SHALL provide 4 reusable agent skills: search_module_content, find_code_examples, get_prerequisites, explain_concept
- Each agent skill SHALL be decorated with @function_tool for use as an agent tool
- The search_module_content skill SHALL accept module_name and query parameters and return relevant text chunks from the specified module
- The find_code_examples skill SHALL accept topic and optional language parameters and return code examples from the book
- The get_prerequisites skill SHALL accept a topic parameter and return prerequisite knowledge information
- The explain_concept skill SHALL accept a concept parameter and return a comprehensive explanation

### FR2: Specialized Subagents
- The system SHALL have 4 specialized subagents: ROS2Agent, SimulationAgent, IsaacAgent, VLAAgent
- Each subagent SHALL have domain-specific expertise as defined in the architecture
- Each subagent SHALL use the reusable agent skills appropriate to its domain
- Each subagent SHALL use module-specific content for its responses
- Each subagent SHALL follow the specific instructions provided for its domain

### FR3: Coordinator Agent & Routing
- The system SHALL have a CoordinatorAgent that analyzes questions and routes to appropriate subagent
- The routing logic SHALL use keyword mapping to determine the appropriate subagent
- The system SHALL have fallback logic to use ROS2Agent when no keywords match
- The routing decision SHALL happen in under 100ms
- The coordinator SHALL return formatted responses with transparency about which subagent was used

### FR4: Backward Compatibility
- The system SHALL maintain backward compatibility with existing chat API
- The response format SHALL remain unchanged (except for optional subagent_used metadata)
- Existing functionality SHALL continue to work without modification
- The new functionality SHALL be accessible through feature flag or optional parameter

### FR5: Integration
- The system SHALL integrate with existing RAG pipeline
- The system SHALL work with existing API endpoints
- The system SHALL maintain existing performance characteristics
- The system SHALL preserve existing error handling patterns

## Success Criteria

### Quantitative Metrics
- 4 specialized subagents successfully implemented
- 4+ reusable agent skills created and functional
- Routing logic working correctly with >95% accuracy
- Routing decision time < 100ms
- Total response time still < 5s
- Answer quality improved compared to general RAG system
- 50 bonus points earned

### Qualitative Measures
- Better answer quality with domain expertise
- More relevant code examples provided
- Focused search with module-specific content
- Reusable agent skills across agents
- Scalable architecture that allows adding more agents
- Professional multi-agent system implementation

## Key Entities

### Agents
- **CoordinatorAgent**: Main agent that analyzes questions and routes to appropriate subagent
- **ROS2Agent**: Specialized agent for ROS 2 related queries
- **SimulationAgent**: Specialized agent for simulation related queries
- **IsaacAgent**: Specialized agent for Isaac related queries
- **VLAAgent**: Specialized agent for Vision-Language-Action related queries

### Agent Skills
- **search_module_content**: Search specific module content in Qdrant
- **find_code_examples**: Find code snippets related to topic
- **get_prerequisites**: Get prerequisite knowledge for a topic
- **explain_concept**: Get detailed explanation of core concept

### Routing Components
- **keyword_mapping**: Mapping of keywords to agent types
- **routing_logic**: Logic to determine appropriate agent based on keywords
- **fallback_strategy**: Default agent when no keywords match

## Assumptions

- The Qdrant vector database has separate collections for each module (module-1-ros2, module-2-simulation, etc.)
- The existing RAG pipeline infrastructure is available for reuse
- The OpenAI SDK with Gemini integration is available for all agents
- The Cohere embedding service is available for all agents
- The system has access to the required API keys for all services
- Module-specific content has been properly indexed in the vector database

## Dependencies

- **Qdrant**: Vector database for module-specific content retrieval
- **Cohere**: Embedding service for semantic search
- **OpenAI SDK**: Interface to Gemini model
- **Existing RAG Pipeline**: Base infrastructure to build upon
- **Configuration**: Settings for API keys and service endpoints