---
sidebar_position: 5
title: "Assignments"
description: "Assignments for Module 2: Digital Twin (Simulation)."
keywords: [simulation, assignments, projects, exercises]
---
# Assignments

This section contains assignments for Module 2.

## Assignment 1: Create a Gazebo World
- **Objective**: Create a simple Gazebo world with a ground plane, a box, and a light source.
- **Tasks**:
  1. Create a new world file.
  2. Add a ground plane, a box, and a light source to the world.
  3. Launch Gazebo and verify that your world is loaded correctly.

## Assignment 2: Spawn a Robot in Gazebo
- **Objective**: Spawn a simple robot model in your Gazebo world.
- **Tasks**:
  1. Create a URDF file for a simple differential drive robot.
  2. Create a launch file that starts Gazebo with your world and spawns the robot.
  3. Verify that the robot is spawned correctly in Gazebo.

## Assignment 3: Control the Robot in Gazebo
- **Objective**: Control the simulated robot in Gazebo using ROS 2.
- **Tasks**:
  1. Add a differential drive plugin to your robot's URDF.
  2. Write a Python node that publishes `geometry_msgs/msg/Twist` messages to the `/cmd_vel` topic.
  3. Run your node and verify that the robot moves in Gazebo.
