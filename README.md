# Imprinting_TurtleBot

ros2 run opencv_ros2 aruco_node_tf --ros-args -p camera_info_topic:=/robot2/camera/camera_info -p image_topic:=/robot2/camera/image_raw


ros2 run opencv_ros2 aruco_node_tf --ros-args -p camera_info_topic:=/robot3/camera/camera_info -p image_topic:=/robot3/camera/image_raw 


ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=/robot1/cmd_vel

ros2 run imprinting_turtlebot imprinting_turtlebot_node 

