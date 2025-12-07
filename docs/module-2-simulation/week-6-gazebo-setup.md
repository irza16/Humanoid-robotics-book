# Week 6: Gazebo Environment Setup

## Overview

This week focuses on setting up and configuring Gazebo simulation environments for humanoid robots. You'll learn to create realistic physics models, configure robot URDF/SDF descriptions for simulation, and implement proper physics properties for accurate simulation behavior.

## Learning Objectives

By the end of this week, you will be able to:

- Install and configure Gazebo Fortress or Garden for humanoid robot simulation
- Convert URDF robot models to SDF for Gazebo simulation
- Configure physics properties including mass, friction, and damping
- Set up Gazebo plugins for ROS 2 integration
- Create custom Gazebo worlds with obstacles and environments

## Gazebo Installation and Setup

### Installing Gazebo

Gazebo comes in different versions. For this module, we'll focus on Gazebo Fortress or Garden:

```bash
# For Ubuntu 22.04
sudo apt update
sudo apt install ros-humble-gazebo-ros-pkgs ros-humble-gazebo-plugins ros-humble-gazebo-dev
sudo apt install gazebo
```

### Verifying Installation

Test that Gazebo is properly installed:

```bash
gazebo
```

You should see the Gazebo GUI with a default empty world.

## URDF to SDF Conversion

Gazebo uses SDF (Simulation Description Format) for simulation models. However, you can load URDF models directly into Gazebo using the robot_state_publisher and joint_state_publisher.

### Basic URDF Requirements for Gazebo

Your URDF model needs specific elements to work properly in Gazebo:

- Links with proper inertial properties (mass, center of mass, inertia tensor)
- Visual and collision geometries for each link
- Gazebo-specific plugins and materials
- Proper joint definitions with dynamics properties

## Physics Configuration

### Inertial Properties

Proper inertial properties are crucial for realistic simulation:

- **Mass**: Should reflect the real robot's mass distribution
- **Inertia**: Diagonal elements (ixx, iyy, izz) should be positive and realistic
- **Center of Mass**: Origin should be at the physical center of mass

### Friction and Contact Properties

Gazebo uses several parameters for contact simulation:

- **mu1 and mu2**: Primary and secondary friction coefficients
- **kp**: Contact stiffness
- **kd**: Contact damping
- **max_vel**: Maximum contact penetration velocity
- **min_depth**: Minimum contact depth before contact is detected

## Gazebo Plugins for ROS 2 Integration

### Joint State Publisher

The joint state publisher plugin publishes joint states from Gazebo to ROS 2 topics.

### Joint Controllers

Gazebo provides plugins for position, velocity, and effort control of joints, allowing ROS 2 nodes to control the simulated robot.

## Creating Custom Worlds

### World File Structure

A Gazebo world file in SDF format includes:

- Physics engine configuration
- Lighting and environment settings
- Models and objects in the scene
- Initial poses and properties

## Launching Gazebo with Your Robot

### Launch File Example

A typical launch file for Gazebo simulation includes:

- Robot state publisher to broadcast transforms
- Gazebo launch with specified world
- Spawn entity to place robot in the world
- Controller managers to handle robot commands

## Debugging Common Issues

### Robot Falls Through Ground

- Check that all links have proper inertial properties
- Verify that collision geometries are defined
- Ensure mass values are positive and realistic

### Robot Jittering or Unstable

- Reduce max_step_size in physics configuration
- Adjust kp (stiffness) and kd (damping) values
- Check for proper joint limits and dynamics

### Joint Control Issues

- Verify that controller plugins are properly configured
- Check that joint names match between URDF and controller configuration
- Ensure proper QoS settings for communication

## Best Practices

1. **Start Simple**: Begin with a basic model and add complexity gradually
2. **Validate Physics**: Test with simple movements before complex behaviors
3. **Use Realistic Parameters**: Base inertial properties on real robot specifications
4. **Test in Isolation**: Debug individual joints and links separately
5. **Monitor Performance**: Adjust physics parameters for optimal simulation speed

## Summary

This week, you've learned to set up Gazebo environments for humanoid robots, configure physics properties, and integrate with ROS 2. These skills form the foundation for advanced simulation work in the coming weeks.

## Next Steps

Next week, you'll learn to integrate Unity for advanced rendering and visualization, enhancing your simulation capabilities with photorealistic graphics.
