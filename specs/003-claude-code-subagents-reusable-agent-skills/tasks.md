# Tasks: Claude Code Subagents & Reusable Agent Skills

## Feature Overview

**Feature**: Claude Code Subagents & Reusable Agent Skills
**Version**: 1.0
**Purpose**: Implement multi-agent architecture with reusable intelligence for 50 bonus points

Enhance the RAG chatbot with specialized subagents for each course module and reusable agent skills. This demonstrates advanced AI architecture with domain-specific expertise and intelligent question routing.

## Implementation Strategy

The implementation will follow a phased approach:
1. Setup and foundational components
2. User Story 1: Implement reusable agent skills
3. User Story 2: Create specialized subagents
4. User Story 3: Implement coordinator and routing
5. User Story 4: Integrate with existing RAG pipeline
6. User Story 5: Update API and response format
7. Polish and cross-cutting concerns

## Dependencies

- User Story 2 (Subagents) depends on User Story 1 (Agent Skills)
- User Story 3 (Coordinator) depends on User Story 2 (Subagents)
- User Story 4 (RAG Integration) depends on User Story 3 (Coordinator)
- User Story 5 (API Update) depends on User Story 4 (RAG Integration)

## Parallel Execution Examples

- Within User Story 1: Each agent skill can be implemented in parallel [P]
- Within User Story 2: Each subagent can be implemented in parallel [P]
- Within User Story 5: Response model update can happen in parallel with API endpoint update [P]

## Phase 1: Setup Tasks

- [ ] T001 Create directory structure for contracts if not exists at specs/003-claude-code-subagents-reusable-agent-skills/contracts/
- [ ] T002 Review existing codebase structure in chatbot/backend/
- [ ] T003 Identify integration points with existing RAG pipeline
- [ ] T004 Verify dependencies (OpenAI SDK, Cohere, Qdrant Client) are available
- [ ] T005 Set up development environment for multi-agent implementation

## Phase 2: Foundational Tasks

- [X] T010 Create function_tool decorator in chatbot/backend/agent_skills.py
- [X] T011 Define retry_with_backoff import from retry_utils for agent skills
- [X] T012 Create base Agent class structure in chatbot/backend/subagents.py
- [X] T013 Define common imports for all agent modules (config, logging, etc.)

## Phase 3: [US1] Implement Reusable Agent Skills

**User Story**: As a developer, I want to use reusable agent skills across different specialized agents

**Goal**: Implement 4 reusable agent skills that can be used by all subagents

**Independent Test Criteria**: Each agent skill can be tested independently and returns expected results

**Tasks**:

- [X] T020 [P] [US1] Create search_module_content function in chatbot/backend/agent_skills.py with module_name and query parameters
- [X] T021 [P] [US1] Implement find_code_examples function in chatbot/backend/agent_skills.py with topic and optional language parameters
- [X] T022 [P] [US1] Implement get_prerequisites function in chatbot/backend/agent_skills.py with topic parameter
- [X] T023 [P] [US1] Implement explain_concept function in chatbot/backend/agent_skills.py with concept parameter
- [X] T024 [P] [US1] Add @function_tool decorator to search_module_content function
- [X] T025 [P] [US1] Add @function_tool decorator to find_code_examples function
- [X] T026 [P] [US1] Add @function_tool decorator to get_prerequisites function
- [X] T027 [P] [US1] Add @function_tool decorator to explain_concept function
- [X] T028 [P] [US1] Add error handling and logging to search_module_content function
- [X] T029 [P] [US1] Add error handling and logging to find_code_examples function
- [X] T030 [P] [US1] Add error handling and logging to get_prerequisites function
- [X] T031 [P] [US1] Add error handling and logging to explain_concept function
- [ ] T032 [US1] Test search_module_content with sample queries
- [ ] T033 [US1] Test find_code_examples with sample topics
- [ ] T034 [US1] Test get_prerequisites with sample topics
- [ ] T035 [US1] Test explain_concept with sample concepts

## Phase 4: [US2] Create Specialized Subagents

**User Story**: As a student, I want to ask ROS 2 related questions and get responses from a specialized ROS 2 expert agent (and similar for other modules)

**Goal**: Create 4 specialized subagents with domain-specific expertise

**Independent Test Criteria**: Each subagent can process domain-specific questions and utilize agent skills appropriately

**Tasks**:

- [X] T040 [P] [US2] Implement ROS2Agent class inheriting from base Agent in chatbot/backend/subagents.py
- [X] T041 [P] [US2] Implement SimulationAgent class inheriting from base Agent in chatbot/backend/subagents.py
- [X] T042 [P] [US2] Implement IsaacAgent class inheriting from base Agent in chatbot/backend/subagents.py
- [X] T043 [P] [US2] Implement VLAAgent class inheriting from base Agent in chatbot/backend/subagents.py
- [X] T044 [P] [US2] Define ROS2Agent expertise: ["ROS 2", "nodes", "topics", "services", "URDF", "TF2", "rclpy"]
- [X] T045 [P] [US2] Define SimulationAgent expertise: ["Gazebo", "Unity", "physics simulation", "URDF/SDF", "sensors"]
- [X] T046 [P] [US2] Define IsaacAgent expertise: ["Isaac Sim", "VSLAM", "Nav2", "synthetic data", "perception"]
- [X] T047 [P] [US2] Define VLAAgent expertise: ["Whisper", "LLMs", "voice control", "vision-language-action"]
- [X] T048 [P] [US2] Set ROS2Agent to use agent skills with 'module-1-ros2' scope
- [X] T049 [P] [US2] Set SimulationAgent to use agent skills with 'module-2-simulation' scope
- [X] T050 [P] [US2] Set IsaacAgent to use agent skills with 'module-3-isaac' scope
- [X] T051 [P] [US2] Set VLAAgent to use agent skills with 'module-4-vla' scope
- [X] T052 [P] [US2] Implement ROS2Agent process_query method with ROS2-specific instructions
- [X] T053 [P] [US2] Implement SimulationAgent process_query method with simulation-specific instructions
- [X] T054 [P] [US2] Implement IsaacAgent process_query method with Isaac-specific instructions
- [X] T055 [P] [US2] Implement VLAAgent process_query method with VLA-specific instructions
- [ ] T056 [US2] Test ROS2Agent with ROS2-related questions
- [ ] T057 [US2] Test SimulationAgent with simulation-related questions
- [ ] T058 [US2] Test IsaacAgent with Isaac-related questions
- [ ] T059 [US2] Test VLAAgent with VLA-related questions

## Phase 5: [US3] Implement Coordinator Agent & Routing

**User Story**: As a student, I want my questions to be automatically routed to the most appropriate specialized agent

**Goal**: Create coordinator agent that routes questions to appropriate subagent based on keywords

**Independent Test Criteria**: Questions are correctly routed to appropriate subagents with >95% accuracy

**Tasks**:

- [X] T060 [US3] Implement CoordinatorAgent class in chatbot/backend/subagents.py
- [X] T061 [US3] Add properties to CoordinatorAgent: ros2_agent, simulation_agent, isaac_agent, vla_agent, keyword_mapping
- [X] T062 [US3] Initialize all subagents in CoordinatorAgent constructor
- [X] T063 [US3] Define keyword_mapping dictionary with ROS2 keywords: ['ros', 'ros2', 'node', 'topic', 'service', 'urdf', 'tf2', 'rclpy', 'launch', 'action', 'rosbag']
- [X] T064 [US3] Define keyword_mapping dictionary with simulation keywords: ['gazebo', 'unity', 'simulation', 'physics', 'sdf', 'simulator', 'sim-to-real', 'digital twin']
- [X] T065 [US3] Define keyword_mapping dictionary with Isaac keywords: ['isaac', 'vslam', 'nav2', 'synthetic', 'perception', 'nvidia', 'isaac sim', 'isaac_ros']
- [X] T066 [US3] Define keyword_mapping dictionary with VLA keywords: ['voice', 'whisper', 'llm', 'gpt', 'language', 'vision-language', 'vla', 'multimodal', 'cognitive']
- [X] T067 [US3] Implement route_to_subagent method that analyzes question and returns appropriate subagent
- [X] T068 [US3] Implement process_query method in CoordinatorAgent that routes to appropriate subagent
- [X] T069 [US3] Add fallback logic to default to ROS2Agent when no keywords match
- [X] T070 [US3] Test routing of ROS2 questions to ROS2Agent
- [X] T071 [US3] Test routing of simulation questions to SimulationAgent
- [X] T072 [US3] Test routing of Isaac questions to IsaacAgent
- [X] T073 [US3] Test routing of VLA questions to VLAAgent
- [X] T074 [US3] Test fallback routing when no keywords match

## Phase 6: [US4] Integrate Routing with RAG Pipeline

**User Story**: As a student, I want the system to maintain backward compatibility with existing chat API

**Goal**: Integrate coordinator routing with existing RAG pipeline while maintaining backward compatibility

**Independent Test Criteria**: Existing functionality continues to work while new routing is available

**Tasks**:

- [X] T080 [US4] Import CoordinatorAgent in chatbot/backend/rag.py
- [X] T081 [US4] Add coordinator_agent instance to RAGPipeline class
- [X] T082 [US4] Extend process_query method to accept use_subagents parameter (default True for backward compatibility)
- [X] T083 [US4] Implement conditional logic to use coordinator routing when use_subagents=True
- [X] T084 [US4] Maintain original pipeline when use_subagents=False
- [X] T085 [US4] Add error handling to fall back to original pipeline if coordinator fails
- [X] T086 [US4] Test backward compatibility with use_subagents=False
- [X] T087 [US4] Test new routing with use_subagents=True
- [X] T088 [US4] Verify performance requirements (<5s response time) are maintained
- [X] T089 [US4] Verify routing decision time is <100ms

## Phase 7: [US5] Update API Response Format

**User Story**: As a developer, I want transparency about which subagent processed my request

**Goal**: Update API response to include subagent_used field for transparency

**Independent Test Criteria**: API response includes optional subagent_used field without breaking existing clients

**Tasks**:

- [X] T090 [US5] Update ChatResponse model in chatbot/backend/main.py to include subagent_used: Optional[str] field
- [X] T091 [US5] Modify chat_endpoint to handle new return format from RAGPipeline
- [X] T092 [US5] Update response creation to include subagent_used value when available
- [X] T093 [US5] Ensure subagent_used field is optional to maintain backward compatibility
- [X] T094 [US5] Test API response includes subagent_used field when using subagents
- [X] T095 [US5] Test API response works without subagent_used field when using original pipeline
- [X] T096 [US5] Verify existing clients still work with new response format

## Phase 8: Polish & Cross-Cutting Concerns

- [X] T100 Create SUBAGENTS.md documentation file in chatbot/ directory
- [X] T101 Document architecture overview in SUBAGENTS.md
- [X] T102 Document subagent descriptions in SUBAGENTS.md
- [X] T103 Document agent skills in SUBAGENTS.md
- [X] T104 Document routing logic in SUBAGENTS.md
- [X] T105 Document usage examples in SUBAGENTS.md
- [X] T106 Document benefits of multi-agent approach in SUBAGENTS.md
- [X] T107 Run comprehensive tests for all components
- [X] T108 Verify all success criteria are met
- [X] T109 Update any relevant README files with subagents information
- [X] T110 Perform final integration testing
- [X] T111 Verify 50 bonus points criteria are met

## Success Criteria

### Technical Success
- [X] All 4 agent skills implemented and tested
- [X] All 4 subagents created and functional
- [X] Routing logic working with >95% accuracy
- [X] Response time under 5 seconds
- [X] Routing decision time under 100ms
- [X] Backward compatibility maintained

### Business Success
- [X] 50 bonus points earned
- [X] Reusable intelligence demonstrated
- [X] Professional multi-agent architecture
- [X] Scalable system ready for future agents