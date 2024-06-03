import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidanceNode(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance_node')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.laser_callback,
            10)
        self.subscription

    def laser_callback(self, msg):
        twist = Twist()
        obstacle_detected = any(r < 1.0 for r in msg.ranges)  # Threshold distance for obstacle detection
        if obstacle_detected:
            twist.linear.x = 0.0
            twist.angular.z = 0.5  # Rotate to avoid obstacle
        else:
            twist.linear.x = 0.5
            twist.angular.z = 0.0
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidanceNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
