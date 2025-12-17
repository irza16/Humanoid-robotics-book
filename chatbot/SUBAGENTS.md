# Multi-Agent Architecture for RAG Chatbot

## Overview

This document describes the multi-agent architecture implemented for the RAG chatbot system. The system uses specialized subagents for different course modules with intelligent routing based on question content.

## Architecture Components

### Coordinator Agent
The main routing component that analyzes questions and routes them to the most appropriate specialized subagent based on keyword matching.

### Specialized Subagents
- **ROS2Expert**: Handles ROS 2 related queries (Module 1)
- **SimulationExpert**: Handles simulation related queries (Module 2)
- **IsaacExpert**: Handles Isaac Sim related queries (Module 3)
- **VLAExpert**: Handles Vision-Language-Action queries (Module 4)

### Agent Skills
Reusable functions available to all subagents:
- `search_module_content`: Search specific module content in Qdrant
- `find_code_examples`: Find code snippets related to a topic
- `get_prerequisites`: Get prerequisite knowledge for a topic
- `explain_concept`: Provide detailed explanation of core concepts

## Agent Skills

### search_module_content(module_name: str, query: str)
Searches for relevant content within a specific module collection in Qdrant. Uses Cohere embeddings for semantic search.

### find_code_examples(topic: str, language: Optional[str] = None)
Finds code snippets related to a specific topic, with optional language filtering.

### get_prerequisites(topic: str)
Retrieves prerequisite knowledge needed to understand a specific topic.

### explain_concept(concept: str)
Provides comprehensive explanations of core concepts from the book content.

## Routing Logic

The CoordinatorAgent uses keyword-based routing to determine the most appropriate subagent:

- **ROS2Agent**: Keywords include 'ros', 'ros2', 'node', 'topic', 'service', 'urdf', 'tf2', 'rclpy', 'launch', 'action', 'rosbag'
- **SimulationAgent**: Keywords include 'gazebo', 'unity', 'simulation', 'physics', 'sdf', 'simulator', 'sim-to-real', 'digital twin'
- **IsaacAgent**: Keywords include 'isaac', 'vslam', 'nav2', 'synthetic', 'perception', 'nvidia', 'isaac sim', 'isaac_ros'
- **VLAAgent**: Keywords include 'voice', 'whisper', 'llm', 'gpt', 'language', 'vision-language', 'vla', 'multimodal', 'cognitive'

If no keywords match, the system defaults to ROS2Agent as the most fundamental.

## Usage Examples

### Using Subagents
```python
# Initialize coordinator
coordinator = CoordinatorAgent()

# Process a question
answer, sources, subagent_used = coordinator.process_query("How do ROS 2 nodes communicate?")
# subagent_used would be "ROS2Expert"
```

### Integration with RAG Pipeline
The system maintains backward compatibility by defaulting to the original pipeline when subagents are disabled:

```python
# Enable subagents (default)
answer, sources, subagent_used = rag_pipeline.process_query(question, selected_text, use_subagents=True)

# Use original pipeline
answer, sources, subagent_used = rag_pipeline.process_query(question, selected_text, use_subagents=False)
```

## Benefits of Multi-Agent Approach

1. **Domain Specialization**: Each agent is optimized for specific content areas
2. **Reusable Intelligence**: Agent skills reduce code duplication and improve maintainability
3. **Intelligent Routing**: Automatic question routing improves response quality
4. **Backward Compatibility**: Existing functionality preserved while adding new features
5. **Scalability**: Easy to add new agents for additional domains
6. **Transparency**: API responses include which subagent was used for processing
7. **Performance**: Minimal routing overhead with fallback mechanisms
8. **Maintainability**: Clear separation of concerns between agents and skills

## Error Handling

- Each agent includes comprehensive error handling with logging
- Fallback to original RAG pipeline if coordinator fails
- Graceful degradation when module-specific collections don't exist
- Robust handling of API failures and network issues

## Configuration

The system uses the following settings from config.py:
- `gemini_api_key`: For LLM calls
- `embedding_model`: For vector embeddings
- `top_k_chunks`: Number of context chunks to retrieve
- `temperature`: For response creativity
- `qdrant_url` and `qdrant_api_key`: For vector database access
- `cohere_api_key`: For embedding generation