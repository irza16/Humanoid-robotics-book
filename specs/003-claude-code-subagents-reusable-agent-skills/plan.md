# Implementation Plan: Claude Code Subagents & Reusable Agent Skills

## Technical Context

**Feature**: Claude Code Subagents & Reusable Agent Skills
**Version**: 1.0
**Purpose**: Implement multi-agent architecture with reusable intelligence for 50 bonus points

### Architecture Overview

The system will implement a multi-agent architecture with:
- 4 specialized subagents (ROS2, Simulation, Isaac, VLA)
- 4 reusable agent skills (search_module_content, find_code_examples, get_prerequisites, explain_concept)
- Coordinator agent for intelligent routing
- Backward compatibility with existing API

### Technology Stack

- Python 3.10+
- FastAPI for web framework
- OpenAI SDK for Gemini integration
- Cohere for embeddings
- Qdrant for vector database
- Existing RAG pipeline infrastructure

### Integration Points

- **chatbot/backend/rag.py**: Primary integration point for routing logic
- **chatbot/backend/main.py**: API endpoint (minimal changes)
- **New files to create**: agent_skills.py, subagents.py, SUBAGENTS.md

### Dependencies

- **Internal**: rag.py, config.py, retry_utils.py
- **External**: OpenAI SDK, Cohere, Qdrant Client
- **Qdrant collections**: module-1-ros2, module-2-simulation, module-3-isaac, module-4-vla

### Unknowns
- Qdrant collection names for module-specific content (NEEDS CLARIFICATION)
- Performance impact of routing logic (NEEDS CLARIFICATION)

## Constitution Check

### Quality Principles
- [x] Code should be testable and maintainable
- [x] Changes should be backward compatible
- [x] Performance should not degrade significantly
- [x] Follow existing code patterns and conventions

### Security Principles
- [x] No changes to authentication/authorization
- [x] Input validation preserved through existing sanitizer
- [x] API key handling unchanged

### Architecture Principles
- [x] Follow single responsibility principle
- [x] Maintain loose coupling between components
- [x] Reuse existing infrastructure where possible

## Gates

### Gate 1: Design Validity
- [x] Feature specification is complete and clear
- [x] Technical approach is feasible
- [x] Dependencies are available

### Gate 2: Architecture Compliance
- [x] Solution maintains backward compatibility
- [x] Follows existing code patterns
- [x] Performance impact is acceptable (<100ms routing)

### Gate 3: Risk Assessment
- [x] Risk of breaking existing functionality is low
- [x] Fallback mechanism is in place
- [x] Testing strategy is comprehensive

## Phase 0: Research & Resolution

### Research Task 1: Qdrant Collection Structure
**Issue**: Need to confirm Qdrant collection names for module-specific content
**Resolution**: Based on the spec, collections should be named: book_content_module-1-ros2, book_content_module-2-simulation, book_content_module-3-isaac, book_content_module-4-vla

### Research Task 2: Performance Impact Assessment
**Issue**: Need to ensure routing logic adds minimal latency
**Resolution**: Routing will use simple keyword matching with O(1) lookup time, should be well under 100ms

### Research Task 3: Integration Approach
**Issue**: How to integrate with existing RAG pipeline
**Resolution**: Extend RAGPipeline class to support routing while maintaining original functionality

## Phase 1: Design & Contracts

### Data Model

#### Agent Skills
- `search_module_content(module_name: str, query: str) -> List[str]`
- `find_code_examples(topic: str, language: Optional[str]) -> List[str]`
- `get_prerequisites(topic: str) -> str`
- `explain_concept(concept: str) -> str`

#### Subagents
- `CoordinatorAgent` - routes questions to appropriate subagent
- `ROS2Agent` - specializes in ROS 2 topics
- `SimulationAgent` - specializes in simulation topics
- `IsaacAgent` - specializes in Isaac topics
- `VLAAgent` - specializes in VLA topics

#### API Response Enhancement
- Add `subagent_used: Optional[str]` field to response for transparency

### API Contracts

#### Routing Logic Contract
```
route_to_subagent(question: str) -> Agent
- Input: user question string
- Output: appropriate specialized agent
- Behavior: keyword-based routing with fallback to ROS2Agent
```

#### Agent Skills Contract
```
Each skill follows the @function_tool decorator pattern
Skills are stateless and idempotent
Skills return structured data as specified
```

### Quickstart Guide

#### Development Setup
1. Create agent_skills.py with reusable skills
2. Create subagents.py with specialized agents
3. Update rag.py with routing logic
4. Test routing with sample questions
5. Verify backward compatibility

#### Testing Approach
- Unit test each agent skill independently
- Test routing logic with sample questions
- Verify all 4 subagents respond appropriately
- Test fallback behavior
- Validate response format remains unchanged

## Phase 2: Implementation Plan

### Phase 2.1: Create Agent Skills Module
**Duration**: 45 minutes
**Deliverable**: chatbot/backend/agent_skills.py

Tasks:
1. Create function_tool decorator
2. Implement search_module_content with module-specific Qdrant queries
3. Implement find_code_examples with code pattern detection
4. Implement get_prerequisites with prerequisite detection
5. Implement explain_concept with deep concept search
6. Add error handling and logging
7. Test each skill independently

### Phase 2.2: Create Subagents Module
**Duration**: 60 minutes
**Deliverable**: chatbot/backend/subagents.py

Tasks:
1. Create base Agent class
2. Implement ROS2Agent with ROS2-specific instructions
3. Implement SimulationAgent with simulation-specific instructions
4. Implement IsaacAgent with Isaac-specific instructions
5. Implement VLAAgent with VLA-specific instructions
6. Create CoordinatorAgent with routing logic
7. Test each agent with sample questions

### Phase 2.3: Integrate Routing with RAG Pipeline
**Duration**: 45 minutes
**Deliverable**: Updated chatbot/backend/rag.py

Tasks:
1. Import subagents and agent skills
2. Add route_to_subagent function with keyword mapping
3. Extend RAGPipeline to support routing
4. Maintain backward compatibility
5. Add subagent_used metadata to responses
6. Test routing functionality

### Phase 2.4: Documentation and Testing
**Duration**: 30 minutes
**Deliverables**: chatbot/SUBAGENTS.md, comprehensive tests

Tasks:
1. Create SUBAGENTS.md with architecture documentation
2. Run all unit tests
3. Run integration tests
4. Verify performance requirements (<5s response time)
5. Verify routing accuracy
6. Test fallback behavior

## Success Criteria

### Technical Success
- [ ] All 4 agent skills implemented and tested
- [ ] All 4 subagents created and functional
- [ ] Routing logic working with >95% accuracy
- [ ] Response time under 5 seconds
- [ ] Routing decision time under 100ms
- [ ] Backward compatibility maintained

### Business Success
- [ ] 50 bonus points earned
- [ ] Reusable intelligence demonstrated
- [ ] Professional multi-agent architecture
- [ ] Scalable system ready for future agents

## Risk Mitigation

### Risk: Performance Degradation
**Mitigation**: Cache agent instances, optimize keyword matching, fallback to original pipeline

### Risk: Incorrect Routing
**Mitigation**: Comprehensive keyword mapping, logging for monitoring, manual override capability

### Risk: Breaking Changes
**Mitigation**: Maintain backward compatibility, extensive testing, gradual rollout capability