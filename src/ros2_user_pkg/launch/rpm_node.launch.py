from launch import LaunchDescription
from launch_ros.actions import Node 
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="ros2_user_pkg",
            executable="rpm_publisher.py",
            name="rpm_node",
            parameters= [
            {"wheel_r" : 3.0}]
        ), 
        Node(
            package="ros2_user_pkg",
            executable="speed_publisher.py",
            name="speed_node"
        ), 
        ExecuteProcess(
            cmd=['ros2', 'topic', 'list'], 
            output="screen"
        )
    ])