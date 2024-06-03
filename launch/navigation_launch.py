from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam',
            executable='slam_node',
            name='slam_node',
            output='screen'
        ),
        Node(
            package='navigation',
            executable='navigation_node',
            name='navigation_node',
            output='screen'
        ),
        Node(
            package='obstacle_avoidance',
            executable='obstacle_avoidance_node',
            name='obstacle_avoidance_node',
            output='screen'
        )
    ])
