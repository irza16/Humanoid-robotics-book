<!-- Sync Impact Report:
Version change: 1.0.0 → 1.1.0
List of modified principles:
- Technical Accuracy First (updated)
- Progressive Difficulty Structure (updated)
- Real-World Applicability (updated)
- Consistent Terminology (updated)
- Original Content with Manufacturer Specifications (updated)
- Setup-Ready Instructions (updated)
Added sections: Content Standards, Tone and Style, Technical Standards (Platform and Tooling, Robotics Standards, AI Standards), Content Architecture, Constraints, Success Criteria
Removed sections: None
Templates requiring updates: ✅ No updates needed - .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
Follow-up TODOs: None
-->
# Physical AI & Humanoid Robotics – Complete Course Book Constitution

## Core Principles

### High technical accuracy across robotics, embodied AI, simulation, and ROS 2 workflows
All robotics concepts (URDF, SLAM, kinematics, sensors, etc.) must follow official ROS 2 and NVIDIA Isaac documentation. All technical definitions must match ROS 2 current LTS & Isaac 2023+. No hallucinated hardware or software features.

### Content optimized for engineering students with CS/AI backgrounds
Content structured for engineering students with CS/AI background. Progressive difficulty: foundations → simulation → embodied intelligence → full humanoid systems.

### Progressive structure: foundations → simulation → embodied intelligence → humanoid robots
Content structured for engineering students with CS/AI background. Progressive difficulty: foundations → simulation → embodied intelligence → full humanoid systems. All modules must be aligned with the 4-part structure.

### Real-world applicability supported by industry-standard tooling
Real-world applicability: everything must map to physical robotics workflows. Hardware recommendations must include VRAM, RAM, CPU, and OS constraints. Every concept should be actionable in real labs (workstation, Jetson kit, robot).

### Consistent terminology across ROS 2, Gazebo, Unity, Isaac Sim, and VLA systems
Consistent terminology across ROS 2, Gazebo, Unity, Isaac, and VLA. Examples must use Python, ROS 2 (rclpy), Gazebo, Unity, Isaac Sim, and Jetson-based workflows.

## Content Standards

### All definitions must follow official ROS 2, NVIDIA Isaac, and robotics documentation
All definitions must follow official ROS 2, NVIDIA Isaac, and robotics documentation. Explanations must balance clarity with technical depth.

### Explanations must balance clarity with technical depth
Explanations must balance clarity with technical depth. Each chapter must include: theory, engineering breakdown, examples, diagrams, and workflows.

### Each chapter must include: theory, engineering breakdown, examples, diagrams, and workflows
Each chapter must include: theory, engineering breakdown, examples, diagrams, and workflows. All diagrams must be markdown-renderable (Mermaid, ASCII, or Spec-Kit diagramming tools).

### All diagrams must be markdown-renderable (Mermaid, ASCII, or Spec-Kit diagramming tools)
All diagrams must be markdown-renderable (Mermaid, ASCII, or Spec-Kit diagramming tools). All modules must align with the 4-part structure.

### All modules must align with the 4-part structure
All modules must align with the 4-part structure:
1. The Robotic Nervous System (ROS 2)
2. The Digital Twin (Simulation in Gazebo + Unity)
3. The AI-Robot Brain (NVIDIA Isaac)
4. Vision-Language-Action (VLA and LLM-Robot interfaces)

## Tone and Style

### Write with engineering clarity (Flesch-Kincaid Grade 10–12)
Write with engineering clarity (Flesch-Kincaid Grade 10–12). Use consistent robotics terminology (no jargon without definition).

### Use consistent robotics terminology (no jargon without definition)
Use consistent robotics terminology (no jargon without definition). Maintain instructional, professional, but friendly tone.

### Maintain instructional, professional, but friendly tone
Maintain instructional, professional, but friendly tone. All code examples in Python (ROS 2 rclpy), plus required configs for Unity/Isaac.

### All code examples in Python (ROS 2 rclpy), plus required configs for Unity/Isaac
All code examples in Python (ROS 2 rclpy), plus required configs for Unity/Isaac.

## Technical Standards

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

### AI Standards
- Use industry-standard datasets or synthetic simulation datasets
- No claims about robot capabilities unless backed by hardware specs
- All examples runnable on:
  • Workstation (RTX 4070 Ti or higher)
  • Jetson Orin Nano/NX
  • Compatible humanoid or quadruped platforms

## Content Architecture

### Modular structure with cross-referenced chapters
Modular structure with cross-referenced chapters. Each module ends with:
• Lab exercises
• Troubleshooting section
• Mini-project

### Each module ends with: Lab exercises, Troubleshooting section, Mini-project
Each module ends with:
• Lab exercises
• Troubleshooting section
• Mini-project

### Final capstone: “The Autonomous Humanoid”
Final capstone: “The Autonomous Humanoid”
• VLA pipeline
• SLAM + navigation
• Vision-based manipulation
• Sim-to-real pipeline

## Governance

### Constraints
- 100% original content
- No hallucinated hardware/software features
- All ROS 2, Unity, Isaac, and robotics workflows must reflect real APIs and tools
- Use only publicly available data or simulation-generated data
- Diagrams must be reproducible with open-source tools

### Success Criteria
- Clear progression from basics → simulation → embodied AI → humanoid robotics
- All content reproducible by students following instructions
- Book deploys cleanly through Docusaurus → GitHub Pages
- Folder-level organization supports Spec-Kit automation
- Chapters support hands-on robotics education with real hardware and digital twins

**Version**: 1.1.0 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-06
