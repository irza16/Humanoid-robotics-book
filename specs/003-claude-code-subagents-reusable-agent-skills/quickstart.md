# Quickstart Guide: Claude Code Subagents & Reusable Agent Skills

## Overview
This guide will help you understand and work with the multi-agent architecture featuring reusable agent skills for the RAG chatbot.

## Architecture Components

### 1. Agent Skills (agent_skills.py)
Reusable functions that all agents can use:

```python
# Search specific module content
search_module_content(module_name: str, query: str) -> List[str]

# Find code examples
find_code_examples(topic: str, language: Optional[str] = None) -> List[str]

# Get prerequisites for a topic
get_prerequisites(topic: str) -> str

# Explain a concept in detail
explain_concept(concept: str) -> str
```

### 2. Specialized Subagents (subagents.py)
Four domain-specific agents:

- **ROS2Agent**: Handles ROS 2 related questions
- **SimulationAgent**: Handles simulation related questions
- **IsaacAgent**: Handles Isaac related questions
- **VLAAgent**: Handles Vision-Language-Action related questions

### 3. Coordinator Agent
Routes questions to the appropriate subagent based on keywords.

## Development Setup

### Prerequisites
- Python 3.10+
- Existing project dependencies (from requirements.txt)
- Access to Qdrant vector database
- API keys for Cohere and Gemini

### File Structure
```
chatbot/
├── backend/
│   ├── agent_skills.py      # Reusable agent skills
│   ├── subagents.py         # Specialized agents
│   ├── rag.py              # Updated with routing logic
│   └── ...                 # Other existing files
└── SUBAGENTS.md            # Architecture documentation
```

## Implementation Steps

### Step 1: Create Agent Skills
```bash
# Create the agent skills module
touch chatbot/backend/agent_skills.py
```

### Step 2: Create Subagents
```bash
# Create the subagents module
touch chatbot/backend/subagents.py
```

### Step 3: Update RAG Pipeline
```bash
# Modify existing RAG pipeline to include routing
# Update chatbot/backend/rag.py
```

### Step 4: Test Implementation
```bash
# Test each agent skill independently
python -c "from chatbot.backend.agent_skills import search_module_content; print(search_module_content('module-1-ros2', 'What is a ROS 2 node?'))"

# Test routing
python -c "from chatbot.backend.subagents import CoordinatorAgent; coordinator = CoordinatorAgent(); agent = coordinator.route_to_subagent('What is a ROS 2 node?'); print(f'Routed to: {agent.name}')"
```

## Testing Strategy

### Unit Tests
1. Test each agent skill independently
2. Test each subagent with sample questions
3. Test routing logic with various keywords
4. Test fallback behavior

### Integration Tests
1. End-to-end: question → route → subagent → response
2. Verify response format remains unchanged
3. Test performance requirements (<5s response time)
4. Test backward compatibility

### Sample Test Questions
```python
# ROS 2 questions
"What is a ROS 2 node?"
"How do ROS 2 topics work?"
"Explain URDF format"

# Simulation questions
"How does Gazebo simulate physics?"
"What is Unity used for in robotics?"

# Isaac questions
"What is Isaac Sim?"
"How does VSLAM work?"

# VLA questions
"What is OpenAI Whisper?"
"How do LLMs control robots?"
```

## Key Features

### 1. Intelligent Routing
The system automatically routes questions to the most appropriate specialized agent based on keywords:

```python
# Example routing
"Tell me about ROS 2 nodes" → ROS2Agent
"How does Gazebo work?" → SimulationAgent
"Explain Isaac Sim" → IsaacAgent
"What is Whisper?" → VLAAgent
```

### 2. Reusable Skills
All agents share the same set of skills, promoting code reuse:

```python
# Each agent can use all skills
agent.search_module_content('module-1-ros2', 'topic')
agent.find_code_examples('publisher', 'python')
agent.get_prerequisites('URDF')
agent.explain_concept('TF2')
```

### 3. Backward Compatibility
The existing API remains unchanged - only the implementation is enhanced:

```python
# Existing calls still work
answer, sources = rag_pipeline.process_query(question, selected_text)
```

## Performance Considerations

- Routing decision time: <100ms
- Total response time: <5s
- Module-specific searches for better relevance
- Caching of agent instances for efficiency

## Troubleshooting

### Routing Issues
- Check keyword mappings in CoordinatorAgent
- Verify question contains recognized keywords
- Fallback agent should handle unrecognized questions

### Performance Issues
- Monitor response times
- Check Qdrant query performance
- Verify Cohere embedding latency

### Compatibility Issues
- Ensure response format matches expectations
- Test with existing frontend clients
- Verify all required fields are present