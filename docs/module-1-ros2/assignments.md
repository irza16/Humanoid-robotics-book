# Module 1 Assignments

## Overview

This document contains all four assignments for Module 1: The Robotic Nervous System (ROS 2). Complete these assignments to demonstrate your understanding of ROS 2 concepts, from basic communication patterns to AI integration.

## Assignment 1: Node Builder

### Description
Create a ROS 2 node that publishes a status message and logs sensor data.

### Requirements
- Create a publisher that broadcasts a status message every 2 seconds
- Create a subscriber that listens to a sensor topic (e.g., JointState, LaserScan, or Imu)
- Log the received sensor data to a file or console
- Implement proper error handling for connection issues
- Use appropriate Quality of Service (QoS) settings

### Success Criteria
- Node successfully publishes status messages at the specified interval
- Node subscribes to and logs sensor data without errors
- Error handling works correctly when sensor topics are unavailable
- Code follows ROS 2 best practices and conventions

### Implementation Tips
- Use rclpy for creating the node
- Implement the node as a class inheriting from rclpy.node.Node
- Use timers for periodic publishing
- Add logging for debugging and monitoring

## Assignment 2: AI-to-ROS Bridge

### Description
Connect a Python AI agent to ROS using rclpy and react to live sensor input.

### Requirements
- Create an AI node that subscribes to sensor data (e.g., LIDAR, camera, or joint states)
- Implement a simple AI algorithm that processes the sensor input
- Based on the AI's analysis, publish appropriate commands (e.g., Twist for movement)
- The AI should demonstrate reactive behavior (responding to sensor changes)
- Include a basic decision-making process

### Success Criteria
- AI node successfully subscribes to sensor data
- AI algorithm processes input and makes decisions
- Appropriate commands are published based on AI decisions
- Behavior changes in response to different sensor inputs
- Code is well-structured and documented

### Implementation Tips
- Consider simple behaviors like obstacle avoidance or object following
- Use basic algorithms like threshold detection or simple neural networks
- Test with simulation data before moving to real sensors
- Implement safety checks to prevent erratic behavior

## Assignment 3: Build a URDF Humanoid

### Description
Construct a simplified humanoid URDF model with joints and collision shapes.

### Requirements
- Create a URDF file defining a basic humanoid robot
- Include at least 10 joints (e.g., hips, knees, shoulders, elbows, neck)
- Define visual and collision properties for each link
- Include appropriate inertial properties for physics simulation
- Use Xacro macros to make the model reusable and maintainable

### Success Criteria
- URDF file loads without errors in RViz
- Robot model displays correctly with all defined joints
- Robot can be visualized in RViz with joint state publisher
- Model includes proper collision and visual elements
- Xacro macros work correctly if used

### Implementation Tips
- Start with a simple base and add complexity gradually
- Use basic geometric shapes (boxes, cylinders, spheres) for links
- Define joints with appropriate types (revolute, continuous, fixed)
- Test the model in RViz to ensure it displays correctly

## Assignment 4: System Launch File

### Description
Create a multi-node launch setup for sensors, controllers, and AI logic.

### Requirements
- Create a Python launch file that starts multiple nodes
- Include at least 4 different nodes (publisher, subscriber, controller, AI)
- Configure appropriate parameters for each node
- Set up proper namespace organization if needed
- Include error handling for node startup failures

### Success Criteria
- Launch file successfully starts all specified nodes
- Nodes communicate correctly with each other
- Parameters are correctly passed to each node
- Launch system handles node failures appropriately
- Overall system behaves as expected

### Implementation Tips
- Use the launch package for creating launch files
- Test individual nodes before creating the launch file
- Include appropriate logging configuration
- Consider using launch conditions for complex startup sequences

## Submission Guidelines

For each assignment:

1. Create a dedicated package in your workspace
2. Include a README.md explaining your implementation
3. Provide launch files where appropriate
4. Include sample outputs or screenshots demonstrating functionality
5. Add comments explaining key implementation decisions

## Evaluation Rubric

Each assignment will be evaluated based on:

- **Functionality** (40%): Does the implementation work as specified?
- **Code Quality** (25%): Is the code well-structured and following ROS 2 conventions?
- **Documentation** (20%): Are comments and documentation clear and helpful?
- **Problem-Solving** (15%): Does the solution demonstrate understanding of ROS 2 concepts?

## Additional Resources

- ROS 2 Documentation: https://docs.ros.org/en/humble/
- TF2 Tutorials: https://docs.ros.org/en/humble/Tutorials/Advanced/Tf2/
- URDF Tutorials: https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/
- Launch Files Guide: https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/

