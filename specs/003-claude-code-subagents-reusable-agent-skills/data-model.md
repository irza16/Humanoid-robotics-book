# Data Model: Claude Code Subagents & Reusable Agent Skills

## Agent Skills

### search_module_content
```
Function: search_module_content(module_name: str, query: str) -> List[str]
Parameters:
  - module_name: Name of the module to search in (e.g., 'module-1-ros2')
  - query: User question to search for
Returns:
  - List of relevant text chunks from the specified module
Behavior:
  - Generates embedding for the query using Cohere
  - Queries Qdrant collection specific to the module
  - Returns top-k text chunks based on similarity
  - Falls back to general collection if module-specific doesn't exist
```

### find_code_examples
```
Function: find_code_examples(topic: str, language: Optional[str] = None) -> List[str]
Parameters:
  - topic: Topic to search for code examples (e.g., 'ROS 2 publisher')
  - language: Optional language filter (e.g., 'python', 'cpp')
Returns:
  - List of code examples from the book
Behavior:
  - Searches for content containing code patterns
  - Filters by language if specified
  - Returns text chunks that likely contain code examples
```

### get_prerequisites
```
Function: get_prerequisites(topic: str) -> str
Parameters:
  - topic: Topic to get prerequisites for (e.g., 'URDF', 'VSLAM')
Returns:
  - Prerequisite information for the topic
Behavior:
  - Searches for prerequisite-related content
  - Returns formatted prerequisite information
  - Provides general recommendation if specific info not found
```

### explain_concept
```
Function: explain_concept(concept: str) -> str
Parameters:
  - concept: Concept to explain (e.g., 'URDF', 'VSLAM', 'TF2')
Returns:
  - Comprehensive explanation of the concept
Behavior:
  - Searches for detailed concept explanations
  - Returns comprehensive explanation from book content
```

## Subagents

### Base Agent Class
```
Class: Agent
Properties:
  - name: Agent identifier
  - expertise: List of topics the agent specializes in
  - instructions: System prompt for the agent
  - client: OpenAI client for LLM calls
Methods:
  - process_query(question: str, selected_text: Optional[str] = None) -> Tuple[str, List[Dict]]
```

### ROS2Agent
```
Class: ROS2Agent (inherits from Agent)
Expertise: ["ROS 2", "nodes", "topics", "services", "URDF", "TF2", "rclpy"]
Instructions: Specialized ROS2 expert instructions
Skills Used: All agent skills with 'module-1-ros2' scope
```

### SimulationAgent
```
Class: SimulationAgent (inherits from Agent)
Expertise: ["Gazebo", "Unity", "physics simulation", "URDF/SDF", "sensors"]
Instructions: Specialized simulation expert instructions
Skills Used: All agent skills with 'module-2-simulation' scope
```

### IsaacAgent
```
Class: IsaacAgent (inherits from Agent)
Expertise: ["Isaac Sim", "VSLAM", "Nav2", "synthetic data", "perception"]
Instructions: Specialized Isaac expert instructions
Skills Used: All agent skills with 'module-3-isaac' scope
```

### VLAAgent
```
Class: VLAAgent (inherits from Agent)
Expertise: ["Whisper", "LLMs", "voice control", "vision-language-action"]
Instructions: Specialized VLA expert instructions
Skills Used: All agent skills with 'module-4-vla' scope
```

## Coordinator Agent

### CoordinatorAgent
```
Class: CoordinatorAgent
Properties:
  - ros2_agent: Instance of ROS2Agent
  - simulation_agent: Instance of SimulationAgent
  - isaac_agent: Instance of IsaacAgent
  - vla_agent: Instance of VLAAgent
  - keyword_mapping: Dictionary mapping keywords to agent types
Methods:
  - route_to_subagent(question: str) -> Agent
  - process_query(question: str, selected_text: Optional[str] = None) -> Tuple[str, List[Dict], str]
```

## API Extensions

### Enhanced Chat Response
```
Class: ChatResponse (extends existing)
Properties:
  - answer: str (existing)
  - sources: List[Source] (existing)
  - session_id: str (existing)
  - subagent_used: Optional[str] (new field for transparency)
```

## Internal Data Structures

### Keyword Mapping
```
Dictionary: keyword_mapping
Structure:
  {
    'ros2': ['ros', 'ros2', 'node', 'topic', 'service', 'urdf', 'tf2', 'rclpy', 'launch', 'action', 'rosbag'],
    'simulation': ['gazebo', 'unity', 'simulation', 'physics', 'sdf', 'simulator', 'sim-to-real', 'digital twin'],
    'isaac': ['isaac', 'vslam', 'nav2', 'synthetic', 'perception', 'nvidia', 'isaac sim', 'isaac_ros'],
    'vla': ['voice', 'whisper', 'llm', 'gpt', 'language', 'vision-language', 'vla', 'multimodal', 'cognitive']
  }
```

### Routing Result
```
Tuple: (answer: str, sources: List[Dict], subagent_used: str)
Description: Extended return format from RAGPipeline that includes which subagent was used
```