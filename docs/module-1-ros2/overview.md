# Module 1: The Robotic Nervous System (ROS 2)

## Overview

Welcome to Module 1, where you'll learn about ROS 2 (Robot Operating System 2), the core middleware that powers modern robots. This module introduces you to how robots communicate internally, how sensors and actuators exchange information, and how AI agents interface with physical systems using rclpy. By the end of this module, you will have developed ROS nodes, built URDF models, and constructed a working robotic "nervous system" for a basic humanoid.

## Learning Outcomes

After completing this module, you will be able to:

- Understand ROS 2 architecture and distributed robotic communication
- Build nodes, topics, services, and actions using Python
- Create robot descriptions using URDF and Xacro
- Use rclpy to connect AI agents to ROS controllers
- Visualize robots and data flow using RViz and TF2
- Write launch files to orchestrate multi-node robot systems
- Debug communication, transforms, and sensor pipelines

## Prerequisites

Before starting this module, you should have:

- Basic Python programming knowledge
- Familiarity with Linux command line interface
- Understanding of fundamental programming concepts (variables, functions, classes)

## Core Concepts

This module covers the following essential ROS 2 concepts:

- **Nodes**: Independent programs that control specific robot subsystems
- **Topics**: Publish/Subscribe channels for continuous robot data streams
- **Services**: Synchronous request/response commands for immediate actions
- **Actions**: Long-running behaviors such as walking or grasping
- **URDF**: XML-based robot description defining links, joints, sensors, and physical structure
- **TF2**: Coordinate transformation system for tracking robot orientation and limb positions
- **rclpy**: Python interface for building ROS 2 nodes and integrating AI models
- **Launch Files**: Orchestration system for running multiple ROS nodes together

## Module Structure

This module is structured over three weeks, each building upon the previous:

- **Week 3**: ROS 2 Foundations - Learn the architecture, workspaces, and basic nodes
- **Week 4**: Sensors, TF, and Robot Models - Explore sensor pipelines, TF2 transforms, and URDF modeling
- **Week 5**: ROS Control & AI Integration - Implement ROS Control and integrate AI agents

## Software Requirements

To complete this module, you'll need:

- ROS 2 Humble or Iron
- Python 3.10+
- RViz 2
- Gazebo (Fortress or Garden)

## Success in This Module

Success in this module will be demonstrated by your ability to create and run 80% of the assigned ROS 2 nodes and communication patterns, construct valid URDF models that can be visualized in RViz without errors, integrate simple Python AI agents with ROS 2, and create launch files that orchestrate multi-node ROS 2 systems with 90% of nodes launching correctly.
