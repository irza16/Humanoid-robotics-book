---
sidebar_position: 5
title: "Assignments"
description: "Assignments for Module 1: ROS 2 Nervous System."
keywords: [ros2, assignments, projects, exercises]
---
# Assignments

This section contains assignments for Module 1.

## Assignment 1: "Hello World" in ROS 2
- **Objective**: Create a simple ROS 2 package with a Python node that publishes a "Hello World" message to a topic.
- **Tasks**:
  1. Create a new ROS 2 package.
  2. Write a Python node that creates a publisher.
  3. Run the node and verify the message is published using `ros2 topic echo`.

## Assignment 2: Service and Client
- **Objective**: Create a ROS 2 service that adds two integers and a client that calls the service.
- **Tasks**:
  1. Create a service definition for adding two integers.
  2. Write a Python node that implements the service.
  3. Write a Python node that calls the service and prints the result.

## Assignment 3: TF2 Broadcaster and Listener
- **Objective**: Create a TF2 broadcaster that publishes a transform between two frames and a listener that subscribes to the transform.
- **Tasks**:
  1. Write a Python node that broadcasts a static transform.
  2. Write a Python node that looks up the transform and prints it.
  3. Visualize the transform in RViz2.
