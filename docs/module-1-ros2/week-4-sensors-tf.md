---
sidebar_position: 3
title: "Week 4: Sensors and TF2"
description: "Integrating sensors and managing coordinate frames with TF2."
keywords: [ros2, sensors, tf2, transforms, lidar, imu]
---
# Week 4: Sensors and TF2

This week focuses on integrating various sensors with ROS 2 and managing coordinate transformations using the TF2 library, essential for understanding a robot's pose and environment.

## Integrating Sensors

Robots use sensors to perceive the world. Common sensors include:
- **LiDAR**: For measuring distances to objects.
- **IMU**: For measuring orientation and acceleration.
- **Cameras**: For capturing images and video.

In ROS 2, sensor data is published on topics. For example, a LiDAR sensor might publish `sensor_msgs/msg/LaserScan` messages on a `/scan` topic.

## TF2 for Coordinate Transforms

A robot is a collection of parts, each with its own coordinate frame. TF2 is a ROS 2 library that helps keep track of these coordinate frames and allows you to transform data between them.

For example, you can use TF2 to transform a laser scan from the frame of the LiDAR to the frame of the robot's base. This is crucial for tasks like navigation and obstacle avoidance.

A transform is represented by a `geometry_msgs/msg/TransformStamped` message, which includes the parent and child frames, and the translation and rotation between them.
