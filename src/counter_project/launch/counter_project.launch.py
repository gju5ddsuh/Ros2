from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='counter_project',
            executable='counter_node',
            name='counter',
            output='screen',
            respawn=True,
            respawn_delay=2
        ),
        Node(
            package='counter_project',
            executable='square_node',
            name='square',
            output='screen'
        ),
        Node(
            package='counter_project',
            executable='logger_node',
            name='logger',
            output='screen'
        ),
        Node(
            package='counter_project',
            executable='reset_service',
            name='reset_service',
            output='screen'
        ),
        Node(
            package='counter_project',
            executable='status_publisher',
            name='status_publisher',
            output='screen'
        ),
    ])
