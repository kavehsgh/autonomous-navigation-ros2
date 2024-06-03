# Autonomous Navigation System with ROS

This project demonstrates the deployment of an autonomous navigation system using ROS. It includes SLAM, path planning, and obstacle avoidance algorithms.

## Features
- SLAM for mapping and localization
- Path planning for navigation
- Obstacle avoidance for safe traversal

## Installation

Clone the repository:

```bash
git clone https://github.com/kavehsgh/autonomous-navigation-ros.git
cd autonomous-navigation-ros
```

Install dependencies:

```bash
sudo apt update
sudo apt install ros-noetic-desktop-full
sudo apt install ros-noetic-navigation ros-noetic-slam-gmapping ros-noetic-move-base
```

## Usage

Launch the navigation system:
```bash
roslaunch navigation_system navigation.launch
```

## Project Structure

- `src/`: Source code for navigation, SLAM, and obstacle avoidance.
- `scripts/`: Auxiliary scripts for setup and utilities.
- `launch/`: ROS launch files.
- `config/`: Configuration files.
- `docs/`: Documentation and tutorials.
