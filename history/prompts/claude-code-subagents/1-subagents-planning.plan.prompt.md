---
id: 1
title: "Subagents Planning"
stage: "plan"
date: "2025-12-17"
model: "claude-sonnet-4-5-20250929"
feature: "claude-code-subagents"
branch: "main"
user: "user"
command: "/sp.plan.subagents"
labels: ["planning", "architecture", "multi-agent"]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - "specs/003-claude-code-subagents-reusable-agent-skills/plan.md"
  - "specs/003-claude-code-subagents-reusable-agent-skills/research.md"
  - "specs/003-claude-code-subagents-reusable-agent-skills/data-model.md"
  - "specs/003-claude-code-subagents-reusable-agent-skills/quickstart.md"
  - "specs/003-claude-code-subagents-reusable-agent-skills/contracts/api-contract.md"
tests: []
outcome: "Successfully created implementation plan for multi-agent architecture with reusable agent skills"
evaluation: "Plan includes all necessary components: agent skills, subagents, routing logic, and documentation"
---

# Prompt

```
/sp.plan.subagents
project: "Claude Code Subagents & Reusable Agent Skills"
timeline: "4 hours"
bonus_points: "50 points"

phases:
  phase_1_agent_skills:
    duration: "Hour 1"
    deliverables:
      - "chatbot/backend/agent_skills.py with 4 reusable skills"
      - "All skills tested independently"

    tasks:
      - "Create agent_skills.py file"
      - "Import function_tool, qdrant, cohere"
      - "Implement search_module_content(module_name, query):"
      - "  - Get embedding for query"
      - "  - Query Qdrant with module filter"
      - "  - Return top 5 text chunks"
      - "Implement find_code_examples(topic, language=None):"
      - "  - Search for chunks containing code blocks"
      - "  - Filter by language if specified"
      - "  - Return code snippets"
      - "Implement get_prerequisites(topic):"
      - "  - Search for prerequisite information"
      - "  - Return formatted prerequisites"
      - "Implement explain_concept(concept):"
      - "  - Deep search for concept explanation"
      - "  - Return comprehensive explanation"
      - "Test each skill independently"

    validation:
      - "All 4 skills have @function_tool decorator"
      - "search_module_content returns relevant chunks"
      - "Skills work with Qdrant collection"

  phase_2_subagents:
    duration: "Hour 2"
    deliverables:
      - "chatbot/backend/subagents.py with 4 specialized agents"
      - "Each agent tested with sample questions"

    tasks:
      - "Create subagents.py file"
      - "Import Agent, model, agent_skills"
      - "Define ros2_agent:"
      - "  - Name: 'ROS2Expert'"
      - "  - Instructions from sp.specify"
      - "  - Tools: all agent skills"
      - "Define simulation_agent:"
      - "  - Name: 'SimulationExpert'"
      - "  - Instructions from sp.specify"
      - "  - Tools: all agent skills"
      - "Define isaac_agent:"
      - "  - Name: 'IsaacExpert'"
      - "  - Instructions from sp.specify"
      - "  - Tools: all agent skills"
      - "Define vla_agent:"
      - "  - Name: 'VLAExpert'"
      - "  - Instructions from sp.specify"
      - "  - Tools: all agent skills"
      - "Test each agent with module-specific question"

    validation:
      - "4 agents created with correct instructions"
      - "All agents use reusable skills"
      - "Each agent responds to test questions"

  phase_3_routing_integration:
    duration: "Hour 3"
    deliverables:
      - "Updated chatbot/backend/rag.py with routing"
      - "Backward compatible chat() function"

    tasks:
      - "Update rag.py"
      - "Import all subagents"
      - "Create route_to_subagent(question) function:"
      - "  - Define keyword mappings from sp.specify"
      - "  - Check question for keywords (case-insensitive)"
      - "  - Return appropriate subagent"
      - "  - Default to ros2_agent if no match"
      - "Update chat(question, selected_text) function:"
      - "  - Get subagent via routing"
      - "  - Run subagent with question"
      - "  - Add 'subagent_used' to response metadata"
      - "  - Keep response format same"
      - "Test routing with all module types"

    validation:
      - "Routing correctly identifies module"
      - "ROS 2 questions → ros2_agent"
      - "Simulation questions → simulation_agent"
      - "Isaac questions → isaac_agent"
      - "VLA questions → vla_agent"
      - "API response format unchanged"

  phase_4_documentation_testing:
    duration: "Hour 4"
    deliverables:
      - "chatbot/SUBAGENTS.md (comprehensive docs)"
      - "All tests passed"
      - "Production deployment"

    tasks:
      - "Create SUBAGENTS.md:"
      - "  - Architecture diagram (ASCII)"
      - "  - Subagent descriptions"
      - "  - Agent skills documentation"
      - "  - Routing logic explanation"
      - "  - Usage examples"
      - "  - Benefits section"
      - "Run comprehensive tests:"
      - "  - Test all 4 subagents"
      - "  - Test routing with 10+ questions"
      - "  - Test reusable skills"
      - "  - Verify response times"
      - "Update main README.md (add subagents section)"
      - "Commit changes"
      - "Deploy to Railway"
      - "Test production"

    validation:
      - "Documentation complete and clear"
      - "All tests pass"
      - "Production deployment successful"
      - "Bonus points criteria met ✅"

testing_strategy:
  skill_tests:
    - "Test search_module_content with each module"
    - "Test find_code_examples returns code"
    - "Test get_prerequisites returns prereqs"
    - "Test explain_concept returns explanation"

  subagent_tests:
    ros2_questions:
      - "What is a ROS 2 node?"
      - "How do ROS 2 topics work?"
      - "Explain URDF format"
    simulation_questions:
      - "How does Gazebo simulate physics?"
      - "What is Unity used for in robotics?"
      - "Explain SDF format"
    isaac_questions:
      - "What is Isaac Sim?"
      - "How does VSLAM work?"
      - "Explain synthetic data generation"
    vla_questions:
      - "What is OpenAI Whisper?"
      - "How do LLMs control robots?"
      - "Explain vision-language-action models"

  routing_tests:
    - "Question with 'ROS 2' → routes to ros2_agent"
    - "Question with 'Gazebo' → routes to simulation_agent"
    - "Question with 'Isaac' → routes to isaac_agent"
    - "Question with 'Whisper' → routes to vla_agent"
    - "Generic question → defaults to ros2_agent"

  integration_tests:
    - "End-to-end: question → route → subagent → response"
    - "Verify response includes subagent metadata"
    - "Verify answer quality improved"
    - "Verify response time < 5s"

file_structure:
  chatbot/backend/
    - agent_skills.py (NEW)
    - subagents.py (NEW)
    - rag.py (UPDATED)
    - main.py (unchanged)
    - database.py (unchanged)
    - config.py (unchanged)
  chatbot/
    - SUBAGENTS.md (NEW)
    - sp.specify.subagents (NEW)
    - sp.plan.subagents (NEW)

technical_notes:
  - "All agents use same Gemini model (cost-effective)"
  - "Agent skills reduce code duplication"
  - "Routing adds minimal latency (< 100ms)"
  - "Backward compatible (existing API unchanged)"
  - "Can disable subagents via feature flag if needed"

risk_mitigation:
  risk_1:
    issue: "Routing might choose wrong subagent"
    solution: "Add logging, allow manual override, improve keywords"

  risk_2:
    issue: "Response time increases"
    solution: "Optimize routing, cache subagent instances"

  risk_3:
    issue: "Breaking existing functionality"
    solution: "Keep backward compatibility, test thoroughly"

success_metrics:
  must_achieve:
    - "4 subagents working"
    - "4 reusable skills created"
    - "Routing logic functional"
    - "Documentation complete"
    - "No breaking changes"

  bonus_criteria:
    - "Demonstrates reusable intelligence ✅"
    - "Demonstrates Claude Code Subagents ✅"
    - "Professional architecture ✅"
    - "Earns 50 bonus points ✅"

deployment_checklist:
  - "agent_skills.py committed"
  - "subagents.py committed"
  - "Updated rag.py committed"
  - "SUBAGENTS.md committed"
  - "Requirements.txt updated (if need
```

# Response

I have successfully created the implementation plan for the Claude Code Subagents & Reusable Agent Skills feature. Here's what was accomplished:

## Created Files:

1. **Implementation Plan**: `specs/003-claude-code-subagents-reusable-agent-skills/plan.md`
   - Technical context with architecture overview
   - Constitution check ensuring quality principles
   - Gates for design validity and risk assessment
   - Detailed phase-by-phase implementation plan

2. **Research Document**: `specs/003-claude-code-subagents-reusable-agent-skills/research.md`
   - Key decisions on Qdrant collection structure
   - Performance optimization strategies
   - Backward compatibility approach
   - Alternative approaches considered

3. **Data Model**: `specs/003-claude-code-subagents-reusable-agent-skills/data-model.md`
   - Detailed function signatures for agent skills
   - Class definitions for subagents
   - API extension specifications
   - Internal data structures

4. **Quickstart Guide**: `specs/003-claude-code-subagents-reusable-agent-skills/quickstart.md`
   - Architecture component explanations
   - Development setup instructions
   - Testing strategy and sample questions
   - Key features and troubleshooting tips

5. **API Contract**: `specs/003-claude-code-subagents-reusable-agent-skills/contracts/api-contract.md`
   - Internal API contracts for agent skills
   - Agent interface specifications
   - Routing interface definitions
   - Performance and error handling contracts

## Key Planning Decisions:

- **Architecture**: Multi-agent system with coordinator routing based on keyword matching
- **Backward Compatibility**: Maintain existing API response format with optional subagent_used field
- **Performance**: Target <100ms routing decision time and <5s total response time
- **Technology**: Reuse existing OpenAI SDK, Cohere, and Qdrant infrastructure
- **Risk Mitigation**: Fallback to original RAG pipeline if routing fails

The implementation plan is comprehensive and ready for the next phase of development.