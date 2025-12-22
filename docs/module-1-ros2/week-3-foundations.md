---
sidebar_position: 2
title: "Week 3: ROS 2 Foundations"
description: "Core concepts of ROS 2, nodes, topics, services, and actions."
keywords: [ros2, foundations, nodes, topics, services, actions]
---
# Week 3: ROS 2 Foundations

This week covers the fundamental concepts of ROS 2, including nodes, topics, services, actions, and the overall ROS graph architecture.

## The ROS 2 Graph

The ROS 2 graph is the network of ROS 2 elements processing data together. It consists of:
- **Nodes**: A process that performs computation. A ROS 2 system is comprised of many nodes.
- **Topics**: Nodes communicate with each other by publishing messages to topics.
- **Services**: A request/response communication pattern.
- **Actions**: For long-running tasks that provide feedback.

## Nodes

A node is the smallest computational unit in ROS 2. It can be a sensor driver, a control algorithm, a perception pipeline, etc. Nodes are typically written in Python or C++.

## Topics

Topics are the buses over which nodes exchange messages. A node can publish messages to a topic, and any node that subscribes to that topic will receive the messages. This is a one-to-many communication pattern.

## Services

Services are used for request/response communication. A node can offer a service, and another node (a client) can send a request and wait for a response. This is a one-to-one communication pattern.

## Actions

Actions are similar to services but are used for long-running tasks. They provide feedback during execution and are preemptible. Examples include navigating to a location, executing a trajectory, etc.
