import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro

def generate_launch_description():

    # 1. Specify the name of the package and the path to the urdf file
    pkg_name = 'my_robot_description'
    file_subpath = 'urdf/robot.urdf'

    # 2. Use xacro to process the file (even if it's just a raw URDF)
    xacro_file = os.path.join(get_package_share_directory(pkg_name), file_subpath)
    robot_description_raw = xacro.process_file(xacro_file).toxml()

    # 3. Configure the Robot State Publisher node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw}]
    )

    # 4. Run the node
    return LaunchDescription([
        node_robot_state_publisher
    ])
