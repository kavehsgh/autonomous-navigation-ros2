import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self.client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.goal_pose = PoseStamped()
        self.goal_pose.header.frame_id = 'map'
        self.goal_pose.pose.position.x = 1.0
        self.goal_pose.pose.position.y = 1.0
        self.goal_pose.pose.orientation.w = 1.0
        self.send_goal()

    def send_goal(self):
        self.get_logger().info('Sending goal')
        self.client.wait_for_server()
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = self.goal_pose
        self.client.send_goal_async(goal_msg)

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
