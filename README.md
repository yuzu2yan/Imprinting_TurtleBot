# Imprinting TurtleBot🦆
![release_date](https://img.shields.io/badge/release_date-Jan_2025-yellow)
[![python](https://img.shields.io/badge/python-v3.10.12-blue)](https://www.python.org/downloads/release/python-31012/)
[![openCV](https://img.shields.io/badge/OpenCV-v4.10.0-blue)](https://opencv.org/blog/opencv-4-10-0/)
[![ROS](https://img.shields.io/badge/ROS-Humble-blue)](https://docs.ros.org/en/humble/index.html)  
[![python](https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat)](https://www.python.org/)
[![linux](https://img.shields.io/badge/-Linux-6C6694.svg?logo=linux&style=flat)](https://www.linux.org/)
[![ubuntu](https://img.shields.io/badge/-Ubuntu-6F52B5.svg?logo=ubuntu&style=flat)](https://releases.ubuntu.com/jammy/)   

Imprinting refers to the habit of an organism to memorize an object moving in front of it as its parent and to follow it thereafter. In this project, Imprinting will be realized using robots. Specifically, multiple robots are lined up in a row, and markers are used to make them follow the previous robot.

<img alt="imprinting" width="600px" src="https://github.com/user-attachments/assets/cc8ac982-0ce0-4930-bb56-1ad2029a8c45">

<img alt="camera" width="600px" src="https://github.com/user-attachments/assets/4db1b3b1-9e64-4e64-a92c-22730095b134">

## Software Configuration
Language : Python 3.10.12  
OS       : Ubuntu 22.04  
ROS      : ROS2 Humble   
OpenCV   : Ver.4.10.0   

<img alt="config" width="600px" src="https://github.com/user-attachments/assets/165d8f81-49ef-400f-90c5-d3b1f87c4f5c">

## Requirements
- Have installed the ROS2 Humble, TurtleBot3, Gazebo, and Nav2 suite of packages.
- Version of `opencv-contrib-python` is `4.5.5.64`

## Quick Start
1. Fix paths in sdf files in `src/imprinting_turtlebot/model/`.
2. Launch Simulation
```
ros2 launch imprinting_turtlebot setup.launch.py
```
3. Recognize arUco markers
```
ros2 run opencv_ros2 aruco_node_tf --ros-args -p camera_info_topic:=/robot2/camera/camera_info -p image_topic:=/robot2/camera/image_raw

// In another terminal
ros2 run opencv_ros2 aruco_node_tf --ros-args -p camera_info_topic:=/robot3/camera/camera_info -p image_topic:=/robot3/camera/image_raw 
```
4. Make the robots follow
```
ros2 run imprinting_turtlebot imprinting_turtlebot_node
```
5. Operate the lead robot
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=/robot1/cmd_vel
```

<img alt="result" width="600px" src="https://github.com/user-attachments/assets/0193da04-3dd7-4329-ad00-9d70f64e2aa0">

## Dependencies
- https://github.com/AI-Robot-Book/chapter5/tree/027a2765154c31ccb6d23f53d4443916760e1141
- https://github.com/JMU-ROBOTICS-VIVA/ros2_aruco/tree/8ec6303acdd0cd5b0def965ac81a9a6ce971fa9a
