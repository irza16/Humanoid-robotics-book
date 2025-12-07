---
sidebar_position: 2
title: "Edge AI Kits"
description: "Compact and efficient hardware for deploying AI models to the edge, focusing on NVIDIA Jetson platforms."
keywords: [hardware, edge ai, jetson, nvidia, orin, nano, nx, realsense]
---

# Edge AI Kits

Edge AI kits provide a compact and power-efficient solution for deploying trained AI models directly on robotic platforms. This section focuses on the NVIDIA Jetson family, which is highly integrated with NVIDIA Isaac ROS and well-suited for embedded robotics applications.

## NVIDIA Jetson Orin Nano

*   **Description**: An entry-level embedded AI computer in the Orin family, offering significant performance improvements over previous generations for small, power-constrained applications.
*   **Price Range**: $199 - $299 (Developer Kit)
*   **Capabilities**: Ideal for basic perception tasks, simple navigation, and running smaller AI models. Supports ROS 2 and Isaac ROS. Good for learning embedded AI.
*   **Limitations**: Limited compute power and memory compared to higher-end Jetsons or workstations. May struggle with complex multi-sensor fusion or large language models.
*   **Required OS/Drivers**: NVIDIA JetPack SDK (includes Ubuntu, CUDA, cuDNN, TensorRT), specific kernel modules for peripherals.
*   **Compatible Modules**: Suitable for introductory examples in Modules 1, 2, and basic perception/inference in Module 3. Can run simplified VLA models in Module 4.

## NVIDIA Jetson Orin NX (8GB / 16GB)

*   **Description**: A powerful, compact System-on-Module (SOM) for advanced robotics and edge AI. Offers more CUDA cores and memory bandwidth than the Nano, enabling more complex AI workloads.
*   **Price Range**: $399 - $599 (Module only, developer kits available)
*   **Capabilities**: Excellent balance of performance and power efficiency. Capable of running more sophisticated perception pipelines, advanced navigation, and medium-sized AI models. Fully supports ROS 2 and Isaac ROS for real-time applications.
*   **Limitations**: Still more constrained than a desktop GPU, making very large model training or high-fidelity simulation impractical directly on the device.
*   **Required OS/Drivers**: NVIDIA JetPack SDK.
*   **Compatible Modules**: Well-suited for all modules, providing a robust platform for most practical examples in Modules 3 and 4.

## Intel RealSense Depth Cameras (D435i / D455)

*   **Description**: A series of stereo depth cameras offering RGB, depth, and infrared data, often including an IMU. Essential for many perception and navigation tasks in robotics.
*   **Price Range**: $200 - $300
*   **Capabilities**: Provides high-quality depth perception for object detection, obstacle avoidance, SLAM, and 3D reconstruction. Integrated IMU helps with odometry and sensor fusion.
*   **Limitations**: Range and accuracy can be affected by ambient light and surface properties. Not suitable for very long-range sensing.
*   **Required OS/Drivers**: librealsense SDK.
*   **Compatible Modules**: Crucial for perception in Modules 1, 3, and 4 (e.g., visual SLAM, object manipulation).

These edge kits, particularly when paired with RealSense cameras, form the backbone of practical embedded robotics development.
