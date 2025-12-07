---
sidebar_position: 5
title: "Module 4: Assignments"
description: "Hands-on assignments for Voice Interface, LLM Agent, and Simulated Grasp, culminating in the Final Capstone Project."
keywords: [module4, assignments, voice interface, llm agent, simulated grasp, capstone]
---

# Module 4: Assignments

This module features a set of challenging assignments designed to solidify your understanding of Vision-Language-Action (VLA) systems and prepare you for the final Capstone Project. Each assignment builds upon the concepts and tools introduced in the weekly lessons.

## Assignments

### 1. The Ear (Voice Interface)

-   **Description**: Create a ROS 2 node that captures audio from a simulated microphone, transcribes it using OpenAI Whisper (or a similar STT service), and publishes the transcribed text to a designated ROS 2 topic. Focus on robust audio handling and accurate transcription.
-   **Learning Outcomes**:
    -   Integrate an STT service into a ROS 2 system.
    -   Manage audio streams and ROS 2 communication.
    -   Handle potential STT transcription errors.

### 2. The Translator (LLM Agent)

-   **Description**: Build a Python-based cognitive agent that subscribes to the transcribed text command (from "The Ear" assignment), queries an LLM (e.g., GPT-4, Claude), and returns a sequence of valid ROS 2 actions in a structured JSON format. Implement safety guardrails to prevent invalid or unsafe actions.
-   **Learning Outcomes**:
    -   Engineer effective prompts for LLMs in a robotic context.
    -   Connect Python-based LLM clients to a ROS 2 system.
    -   Implement JSON parsing and validation for structured robot commands.
    -   Develop safety mechanisms for AI-driven robot control.

### 3. Simulated Grasp

-   **Description**: Program the humanoid arm in a simulated environment (e.g., NVIDIA Isaac Sim, Gazebo with MoveIt 2) to identify a target object (using visual perception data from Module 3) and execute a pick-and-place maneuver. This assignment will integrate arm kinematics, motion planning, and object interaction.
-   **Learning Outcomes**:
    -   Implement Inverse Kinematics for a multi-jointed robot arm.
    -   Utilize a robotic motion planning framework (e.g., MoveIt 2).
    -   Integrate vision-based object detection with manipulation tasks.
    -   Perform pick-and-place operations in a simulated environment.

## Final Capstone Project: The Autonomous Humanoid

-   **Summary**: The ultimate challenge! Integrate all components from Modules 0-4 to create a fully autonomous humanoid robot. The robot should be able to:
    1.  Listen to natural language voice commands from a user.
    2.  Cognitively plan complex tasks based on these commands using the LLM agent.
    3.  Perceive its environment and objects using its vision system (from Module 3).
    4.  Dynamically adapt its plan based on real-time visual feedback.
    5.  Execute physical actions (locomotion, manipulation) via ROS 2.
    6.  Demonstrate the full "Sense-Think-Act" loop in a compelling scenario.
-   **Scenario**: The robot is in a room with various objects. A user gives it a high-level command (e.g., "Clean up the blue blocks and put them in the box," or "Fetch me the water bottle from the table"). The robot must interpret, plan, and execute the task autonomously, handling any unexpected events.
-   **Deliverables**: A functioning integrated system in simulation, a project report detailing the architecture and implementation, and a video demonstration of the robot successfully completing the capstone scenario.
