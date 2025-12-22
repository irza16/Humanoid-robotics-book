# Week 4: Sensors, TF, and Robot Models

## Overview

Welcome to Week 4 of the Robotic Nervous System module! This week focuses on sensor integration, coordinate transformations with TF2, and robot modeling using URDF (Unified Robot Description Format). You'll learn how robots perceive their environment through various sensors, how to manage coordinate systems for multi-part robots, and how to create digital representations of physical robots.

## Learning Objectives

By the end of this week, you will be able to:

- Stream and process sensor data in ROS 2
- Implement and use TF2 transforms for coordinate system management
- Create robot descriptions using URDF and Xacro
- Visualize robots and sensor data in RViz
- Debug sensor pipelines and transform issues

## Sensor Streaming Pipelines

Robots rely on various sensors to perceive their environment. In ROS 2, sensors publish data to topics that other nodes can subscribe to. Common sensor types include:

- **Camera sensors**: Publish image data as sensor_msgs/Image
- **LIDAR sensors**: Publish point clouds as sensor_msgs/LaserScan or sensor_msgs/PointCloud2
- **IMU sensors**: Publish inertial measurements as sensor_msgs/Imu
- **Joint state sensors**: Publish joint positions as sensor_msgs/JointState

### Camera Sensor Pipeline

Camera sensors typically publish images to topics like /camera/image_raw. To process these images, you need to convert them from ROS Image messages to OpenCV images using cv_bridge.

### LIDAR Sensor Pipeline

LIDAR sensors publish laser scan data to topics like /scan. This data can be used for obstacle detection, mapping, and navigation.

## TF2 Transforms and Coordinate Frames

TF2 (Transform Library 2) is ROS 2's system for managing coordinate frame transformations. It allows you to keep track of multiple coordinate frames over time and answer questions like "What is the position of the robot's gripper relative to the camera?"

### Understanding Coordinate Frames

In robotics, coordinate frames define the position and orientation of objects in space. Common frames include:

- **map**: Fixed world coordinate frame
- **odom**: Odometry-based coordinate frame
- **base_link**: Robot's base coordinate frame
- **camera_frame**: Camera's coordinate frame
- **laser_frame**: LIDAR's coordinate frame

### TF2 Publisher

To publish transforms between frames, you use a TransformBroadcaster. This is typically done in a timer callback to continuously update the transform.

### TF2 Lookup

To lookup transforms between frames, you use a TransformListener. This allows you to query the transform between two frames at a specific time.

## URDF and Xacro for Robot Modeling

URDF (Unified Robot Description Format) is an XML format for representing robot models. It defines the physical and visual properties of robots, including links, joints, and sensors.

### Basic URDF Structure

A basic URDF file contains:
- Links: Rigid bodies of the robot
- Joints: Connections between links
- Visual: How the robot looks in simulation
- Collision: Collision properties for physics simulation
- Inertial: Mass and inertia properties

### Xacro for Complex Models

Xacro is an XML macro language that allows you to create more complex and reusable URDF models. It provides features like:
- Property definitions
- Macros for reusable components
- Mathematical expressions
- File inclusion

## RViz Visualization

RViz is ROS 2's 3D visualization tool for displaying robot models, sensor data, and other information. You can add different displays to visualize:
- Robot models (RobotModel)
- Sensor data (LaserScan, Image, PointCloud2)
- Transforms (TF)
- Paths and goals (Path, Pose)
- Grids and markers

## Debugging Sensor Pipelines and Transforms

### Common Sensor Issues

- **No data**: Check if sensor driver is running and publishing
- **Wrong frame**: Verify sensor frame_id matches expected transform
- **Wrong data type**: Ensure subscriber expects correct message type

### TF2 Debugging Commands

- ros2 run tf2_tools view_frames: View the transform tree
- ros2 run tf2_ros tf2_echo base_link laser_frame: Echo transforms
- ros2 run tf2_ros tf2_monitor: Check for transform errors

## Summary and Next Steps

This week, you've learned how to work with sensor data, manage coordinate systems with TF2, create robot models with URDF/Xacro, and visualize your robots in RViz. These skills are essential for building complex robotic systems that can perceive and interact with their environment.

Next week, we'll explore ROS Control for managing robot hardware and integrating AI agents with physical systems.

## Key Takeaways

- Sensors publish data to topics for other nodes to process
- TF2 manages coordinate frame transformations between robot parts
- URDF describes robot geometry, kinematics, and dynamics
- RViz provides 3D visualization of robots and sensor data
- Proper debugging tools help identify sensor and transform issues
