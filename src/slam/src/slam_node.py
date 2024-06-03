import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid

class SlamNode(Node):
    def __init__(self):
        super().__init__('slam_node')
        self.subscription = self.create_subscription(
            OccupancyGrid,
            'map',
            self.map_callback,
            10)
        self.subscription

    def map_callback(self, msg):
        self.get_logger().info('Received map data')

def main(args=None):
    rclpy.init(args=args)
    node = SlamNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
