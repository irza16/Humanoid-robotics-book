---
id: 1
title: "Update constitution for Physical AI & Humanoid Robotics course"
stage: constitution
date: "2025-12-06"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "main"
user: "user"
command: "/sp.constitution"
labels: ["constitution", "setup", "principles"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - ".specify/memory/constitution.md"
tests: []
---

# Prompt

```
Project: Physical AI & Humanoid Robotics – Complete Course Book

Core principles:
- High technical accuracy in robotics, ROS 2, Isaac, and simulation systems
- Content structured for engineering students with CS/AI background
- Real-world applicability: everything must map to physical robotics workflows
- Progressive difficulty: theory → simulation → embodied AI → full humanoid systems
- Consistent terminology across ROS 2, Gazebo, Unity, Isaac, and VLA

Key standards:
- All robotics concepts (URDF, SLAM, kinematics, sensors, etc.) must follow official ROS 2 and NVIDIA Isaac documentation
- Hardware recommendations must include VRAM, RAM, CPU, and OS constraints
- All modules must be aligned with the provided quarter structure (Weeks 1–13)
- Examples must use Python, ROS 2 (rclpy), Gazebo, Unity, Isaac Sim, and Jetson-based workflows
- Diagrams must represent: robot architecture, digital twin pipeline, sensor stack, ROS graph, and VLA pipelines

Content structure:
- 4 core modules:
  1. The Robotic Nervous System (ROS 2)
  2. The Digital Twin (Gazebo & Unity)
  3. The AI-Robot Brain (NVIDIA Isaac)
  4. Vision-Language-Action (VLA)

- Each module must include:
  • Theory explanation
  • Engineering breakdown
  • Tools used (ROS 2/Gazebo/Unity/Isaac/Jetson/etc.)
  • Example workflows
  • Code samples
  • Troubleshooting
  • Mini-project at the end

- Capstone chapter: "The Autonomous Humanoid"
  Must include:
  • Voice-to-action pipeline
  • Natural language → ROS 2 task planning
  • Navigation & SLAM
  • Object detection & manipulation
  • Sim-to-real transfer flow

Hardware guidelines:
- Include 3 tiers:
  • Digital Twin Workstation (RTX 4070 Ti minimum)
  • Edge Kits (Jetson Orin Nano/NX + RealSense)
  • Robot Lab Options (Unitree Go2, G1, OP3, TonyPi, etc.)

- Every hardware section must include:
  • Price range
  • What it can and cannot do
  • Required OS and drivers
  • Compatible modules in the course

Constraints:
- 100% original content
- No hallucinated hardware or software features
- All technical definitions must match ROS 2 Humble/Iron & Isaac 2023+
- No claims about humanoid capabilities unless backed by manufacturer specs
- All diagrams auto-generated using markdown-compatible syntax

Success criteria:
- Course flows from foundational robotics → simulation → AI → embodied intelligence
- Hardware and software instructions are setup-ready for students
- Each chapter prepares the student for the capstone humanoid robot project
- Book must be clear enough for self-learners but deep enough for capstone-level engineering
- Every concept should be actionable in real labs (workstation, Jetson kit, robot)
```

# Response

The constitution for the Physical AI & Humanoid Robotics course book project has been successfully updated. The new constitution includes:

## Core Principles
- Technical Accuracy First: All robotics concepts must follow official ROS 2 and NVIDIA Isaac documentation
- Progressive Difficulty Structure: Content structured for engineering students with CS/AI background
- Real-World Applicability: Everything maps to physical robotics workflows
- Consistent Terminology: Across ROS 2, Gazebo, Unity, Isaac, and VLA
- Original Content with Manufacturer Specifications: 100% original content with manufacturer specs
- Setup-Ready Instructions: Hardware and software instructions are setup-ready for students

## Content Structure Requirements
- 4 core modules: The Robotic Nervous System (ROS 2), The Digital Twin (Gazebo & Unity), The AI-Robot Brain (NVIDIA Isaac), Vision-Language-Action (VLA)
- Each module includes: Theory explanation, Engineering breakdown, Tools used, Example workflows, Code samples, Troubleshooting, Mini-project at the end

## Development Workflow
- Each module must include theory explanation, engineering breakdown, tools used, example workflows, code samples, troubleshooting, and a mini-project at the end
- All diagrams must be auto-generated using markdown-compatible syntax

The constitution is now in place to guide the development of the Physical AI & Humanoid Robotics course book project.

# Outcome

The project constitution has been successfully created and implemented, providing clear principles and guidelines for the development of the Physical AI & Humanoid Robotics course book. This will ensure consistency and quality throughout the project development process.
