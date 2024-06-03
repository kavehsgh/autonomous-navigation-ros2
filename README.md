# Autonomous Navigation System with ROS

This project demonstrates the deployment of an autonomous navigation system using ROS. It includes SLAM, path planning, and obstacle avoidance algorithms.

## Features
- SLAM for mapping and localization
- Path planning for navigation
- Obstacle avoidance for safe traversal

## Installation

Clone the repository:

```bash
git clone https://github.com/kavehsgh/autonomous-navigation-ros2.git
cd autonomous-navigation-ros2
```

Install ROS2 Humble and Nav2:

```bash
sudo apt update
sudo apt install ros-noetic-desktop-full
sudo apt install ros-noetic-navigation ros-noetic-slam-gmapping ros-noetic-move-base
```

Build the workspace:

```bash
colcon build
```

## Usage

Source the setup file:

```bash
source install/setup.bash
```


Launch the navigation system:

```bash
ros2 launch navigation_system navigation_launch.py
```

## Project Structure

- `src/`: Source code for navigation, SLAM, and obstacle avoidance.
- `launch/`: ROS launch files.
- `config/`: Configuration files.
- `docs/`: Documentation and tutorials.



#### Implementation

1. **SLAM Implementation:**

- Create a ROS2 package for SLAM:
  
```bash
cd src
ros2 pkg create --build-type ament_python slam
cd slam/slam
mkdir src
```

- Implement SLAM using `slam_toolbox`:
Example: src/slam/slam_node.py


2. **Path Planning with Nav2:**

- Create a ROS2 package for navigation:

```bash
cd ../..
ros2 pkg create --build-type ament_python navigation
cd navigation/navigation
mkdir src
```
Implement path planning using Nav2.
Example: 'src/navigation/navigation_node.py'


3. **Obstacle Avoidance:**

- Create a ROS2 package for obstacle avoidance:
```bash
cd ..
catkin_create_pkg obstacle_avoidance rospy std_msgs sensor_msgs geometry_msgs
mkdir -p obstacle_avoidance/src
```

Implement obstacle avoidance using sensor data:
Example: 'src/obstacle_avoidance/obstacle_avoidance_node.py'

4. **Launch Files:**

Create launch files for each component in the launch directory.
Example: 'launch/navigation_launch.py'

