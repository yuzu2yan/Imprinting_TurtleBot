import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from ros2_aruco_interfaces.msg import ArucoMarkers

class ArucoPoseSubscriber(Node):

    def __init__(self):
        super().__init__('aruco_pose_subscriber')
        self.subscription = self.create_subscription(
            ArucoMarkers,
            '/aruco_markers',
            self.aruco_pose_callback,
            10)
        
        # Create publishers to send velocity commands
        self.cmd_vel_publisher2 = self.create_publisher(Twist, '/robot2/cmd_vel', 10)
        self.cmd_vel_publisher3 = self.create_publisher(Twist, '/robot3/cmd_vel', 10)
        
    def aruco_pose_callback(self, msg):
        # Iterate through marker IDs and corresponding poses
        for marker_id, pose in zip(msg.marker_ids, msg.poses):
            position = pose.position

            # Create a Twist message to send velocity commands
            twist = Twist()

            if position.x > 0.1:
                twist.linear.x = 0.2
                twist.angular.z = -0.5  # Turn right
            elif position.x < -0.1:
                twist.linear.x = 0.2
                twist.angular.z = 0.5  # Turn left
            elif position.z > 0.3:
                twist.linear.x = 0.2  # Move forward
            else:
                twist.linear.x = 0.0
                twist.angular.z = 0.0

            # Publish the velocity command based on marker ID
            if marker_id == 1:
                self.cmd_vel_publisher2.publish(twist)
            elif marker_id == 2:
                self.cmd_vel_publisher3.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    aruco_pose_subscriber = ArucoPoseSubscriber()
    rclpy.spin(aruco_pose_subscriber)
    aruco_pose_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
