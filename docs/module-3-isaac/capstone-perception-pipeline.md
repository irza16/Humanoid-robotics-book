---
sidebar_position: 6
title: "Capstone: Perception Pipeline"
description: "Capstone project for Module 3: Building a full perception pipeline in Isaac Sim."
keywords: [isaac, capstone, project, perception, pipeline]
---
# Capstone: Perception Pipeline

This capstone project involves building a complete perception and navigation pipeline for a robot in Isaac Sim, from sensor data to autonomous action.

## Project Goal

The goal of this project is to create a ROS 2 system that can autonomously navigate a simulated robot to a target object in a cluttered environment.

## Components

You will need to create the following components:
- An **object detection node** that uses a DNN to detect the target object.
- A **localization node** that estimates the robot's pose in the environment.
- A **path planning node** that generates a path to the target object.
- A **control node** that follows the planned path while avoiding obstacles.

## Simulation

You will use Isaac Sim to create a simulation environment with a robot, a target object, and several obstacles. You will also use Isaac Sim to generate synthetic data for training your object detection model.

## Evaluation

Your project will be evaluated based on the following criteria:
- **Functionality**: Does the robot successfully navigate to the target object without colliding with obstacles?
- **Performance**: How quickly and efficiently does the robot reach the target?
- **AI Integration**: Does the project effectively use AI for perception and navigation?
