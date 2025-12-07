---
id: 001
title: Update Humanoid Robotics Book Constitution
stage: constitution
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: user
command: /sp.constitution
labels: [constitution, update]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md
tests:
null
---

## Prompt

/sp.constitution

Project: Physical AI & Humanoid Robotics – Complete Course Book

Core Principles:
- High technical accuracy across robotics, embodied AI, simulation, and ROS 2 workflows
- Content optimized for engineering students with CS/AI backgrounds
- Progressive structure: foundations → simulation → embodied intelligence → humanoid robots
- Real-world applicability supported by industry-standard tooling
- Consistent terminology across ROS 2, Gazebo, Unity, Isaac Sim, and VLA systems

Content Standards:
- All definitions must follow official ROS 2, NVIDIA Isaac, and robotics documentation
- Explanations must balance clarity with technical depth
- Each chapter must include: theory, engineering breakdown, examples, diagrams, and workflows
- All diagrams must be markdown-renderable (Mermaid, ASCII, or Spec-Kit diagramming tools)
- All modules must align with the 4-part structure:
  1. The Robotic Nervous System (ROS 2)
  2. The Digital Twin (Simulation in Gazebo + Unity)
  3. The AI-Robot Brain (NVIDIA Isaac)
  4. Vision-Language-Action (VLA and LLM-Robot interfaces)

Tone and Style:
- Write with engineering clarity (Flesch-Kincaid Grade 10–12)
- Use consistent robotics terminology (no jargon without definition)
- Maintain instructional, professional, but friendly tone
- All code examples in Python (ROS 2 rclpy), plus required configs for Unity/Isaac

Technical Standards:

### Platform and Tooling
- **Publishing Platform**: Docusaurus
- **Deployment Target**: GitHub Pages
- **Development Framework**: Spec-Kit Plus + Claude Code
- **Version Control**: Git with structured commit history (conventional commits recommended)

### Robotics Standards
- **Framework**: ROS 2 (current LTS)
- **Model Format**: URDF (Unified Robot Description Format)
- **Control Systems**: PID, trajectory planning, sensor fusion, perception pipelines
- **Simulation**: Gazebo (Fortress/Iron), Unity Robotics Hub, Isaac Sim
- **AI Frameworks**: NVIDIA Isaac ROS, Isaac Sim, Foundation models (VLA)
- **Kinematics**: Forward/inverse kinematics, IK solvers, DH parameters
- **Sensing**: RealSense, LiDAR, IMU, RGB-D, proprioceptive sensors
- **Navigation**: SLAM, Nav2, occupancy grids, global/local planners

AI Standards:
- Use industry-standard datasets or synthetic simulation datasets
- No claims about robot capabilities unless backed by hardware specs
- All examples runnable on:
  • Workstation (RTX 4070 Ti or higher)
  • Jetson Orin Nano/NX
  • Compatible humanoid or quadruped platforms

Content Architecture:
- Modular structure with cross-referenced chapters
- Each module ends with:
  • Lab exercises
  • Troubleshooting section
  • Mini-project
- Final capstone: “The Autonomous Humanoid”
  • VLA pipeline
  • SLAM + navigation
  • Vision-based manipulation
  • Sim-to-real pipeline

Constraints:
- 100% original content
- No hallucinated hardware/software features
- All ROS 2, Unity, Isaac, and robotics workflows must reflect real APIs and tools
- Use only publicly available data or simulation-generated data
- Diagrams must be reproducible with open-source tools

Success Criteria:
- Clear progression from basics → simulation → embodied AI → humanoid robotics
- All content reproducible by students following instructions
- Book deploys cleanly through Docusaurus → GitHub Pages
- Folder-level organization supports Spec-Kit automation
- Chapters support hands-on robotics education with real hardware and digital twins

## Response snapshot

The project constitution has been updated to version 1.1.0.

## Outcome

- ✅ Impact: Constitution updated with new principles and content.
- 🧪 Tests: No tests run for constitution update.
- 📁 Files: Updated .specify/memory/constitution.md
- 🔁 Next prompts: null
- 🧠 Reflection: Successfully updated the project constitution based on user's input, incorporating all provided sections and managing versioning.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
