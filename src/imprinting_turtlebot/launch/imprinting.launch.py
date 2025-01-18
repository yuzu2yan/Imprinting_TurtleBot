import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import PushRosNamespace
from launch_ros.actions import Node

def generate_launch_description():
    imprinting_dir = get_package_share_directory('imprinting_turtlebot')
    robot_sdf1 = os.path.join(
        imprinting_dir, 'model1.sdf'
    )
    robot_sdf2 = os.path.join(
        imprinting_dir, 'model2.sdf'
    )
    robot_sdf3 = os.path.join(
        imprinting_dir, 'model3.sdf'
    )
    urdf = os.path.join(imprinting_dir, 'turtlebot3_waffle.urdf')
    with open(urdf, 'r') as infp:
        robot_description = infp.read()
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    world = os.path.join(
        imprinting_dir, 'empty_world.world'
    )
    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )
    
    remappings = [('/tf', 'tf'),
                  ('/tf_static', 'tf_static')]
    
    start_robot_state_publisher_cmd1 = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace='/robot1',
        output='screen',
        parameters=[{'use_sim_time': True,
                     'robot_description': robot_description}],
        remappings=remappings,
        respawn=True)

    start_gazebo_spawner_cmd1 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        output='screen',
        arguments=[
            '-entity', 'tb1',
            '-file', robot_sdf1,
            '-robot_namespace', '/robot1',
            '-x', '0.0', '-y', '-0.5', '-z', '0.01',
            '-R', '0.00', '-P', '0.00', '-Y', '0.00'],
        respawn=True)
    
    start_robot_state_publisher_cmd2 = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace='/robot2',
        output='screen',
        parameters=[{'use_sim_time': True,
                     'robot_description': robot_description}],
        remappings=remappings,
        respawn=True)

    start_gazebo_spawner_cmd2 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        output='screen',
        arguments=[
            '-entity', 'tb2',
            '-file', robot_sdf2,
            '-robot_namespace', '/robot2',
            '-x', '-1.5', '-y', '-0.5', '-z', '0.01',
            '-R', '0.00', '-P', '0.00', '-Y', '0.00'],
        respawn=True)
    
    start_robot_state_publisher_cmd3 = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace='/robot3',
        output='screen',
        parameters=[{'use_sim_time': True,
                     'robot_description': robot_description}],
        remappings=remappings,
        respawn=True)

    start_gazebo_spawner_cmd3 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        output='screen',
        arguments=[
            '-entity', 'tb3',
            '-file', robot_sdf3,
            '-robot_namespace', '/robot3',
            '-x', '-3.5', '-y', '-0.5', '-z', '0.01',
            '-R', '0.00', '-P', '0.00', '-Y', '0.00'],
        respawn=True)

    ld = LaunchDescription()

    # Add the commands to the launch description
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)

    # Add the robot groups    
    ld.add_action(start_robot_state_publisher_cmd1)
    ld.add_action(start_gazebo_spawner_cmd1)
    
    ld.add_action(start_robot_state_publisher_cmd2)
    ld.add_action(start_gazebo_spawner_cmd2)
    
    ld.add_action(start_robot_state_publisher_cmd3)
    ld.add_action(start_gazebo_spawner_cmd3)

    return ld