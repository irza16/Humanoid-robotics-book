---
sidebar_position: 3
title: "Week 9: Perception"
description: "Implementing perception pipelines with Isaac ROS."
keywords: [isaac ros, perception, object detection, segmentation, nvidia]
---
# Week 9: Perception

This week focuses on implementing advanced perception pipelines using Isaac ROS gems for tasks like object detection, image segmentation, and 3D reconstruction.

## Isaac ROS Gems

Isaac ROS is a collection of hardware-accelerated packages for ROS 2 that are optimized for NVIDIA's Jetson platform and GPUs. These packages, called "gems," provide a wide range of capabilities for building high-performance robotics applications.

Some of the key perception gems include:
- **`isaac_ros_image_proc`**: for hardware-accelerated image processing, including rectification and resizing.
- **`isaac_ros_apriltag`**: for detecting AprilTags, which are commonly used for localization and object tracking.
- **`isaac_ros_dnn_inference`**: for running deep neural network (DNN) models for tasks like object detection and image segmentation.
- **`isaac_ros_visual_slam`**: for visual SLAM (Simultaneous Localization and Mapping), which allows a robot to build a map of its environment and track its position within it.

## Building a Perception Pipeline

You can combine these gems to create a powerful perception pipeline. For example, you could create a pipeline that takes an image from a camera, runs an object detection model to identify objects in the scene, and then publishes the results on a ROS 2 topic.

By leveraging the hardware acceleration provided by Isaac ROS, you can build perception pipelines that run in real-time on embedded platforms like the NVIDIA Jetson.
