---
sidebar_position: 6
title: "Capstone: Nervous System"
description: "Capstone project for Module 1: Building a complete ROS 2 nervous system."
keywords: [ros2, capstone, project, nervous system]
---
# Capstone: Nervous System

This capstone project involves building a complete ROS 2-based "nervous system" for a simulated robot, integrating nodes, topics, services, and transforms.

## Project Goal

The goal of this project is to create a ROS 2 system that can control a simulated robot to perform a simple task, such as moving to a specified location while avoiding obstacles.

## Components

You will need to create the following components:
- A **control node** that publishes velocity commands.
- A **sensor node** that processes laser scan data to detect obstacles.
- A **TF2 broadcaster** to publish the robot's coordinate frames.
- A **launch file** to start all the nodes.

## Simulation

You will use a simple robot model in a simulated environment (e.g., Gazebo) to test your system.

## Evaluation

Your project will be evaluated based on the following criteria:
- **Functionality**: Does the robot successfully navigate to the goal without colliding with obstacles?
- **Code Quality**: Is the code well-structured, documented, and easy to understand?
- **ROS 2 Best Practices**: Does the project follow ROS 2 conventions and best practices?
