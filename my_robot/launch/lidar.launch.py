import os
from launch import LaunchDescription
from launch_ros.actions import Node

# def generate_launch_description():

#     return LaunchDescription([

#         Node(
#             package='rplidar_ros',
#             executable='rplidar_composition',
#             output='screen',
#             parameters=[{
#                 'serial_port': '/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.3:1.0-port0',
#                 'frame_id': 'laser_frame',
#                 'angle_compensate': True,
#                 'scan_mode': 'Standard'
#             }]
#         )
#     ])

def generate_launch_description():
  # LDROBOT LiDAR publisher node
  ldlidar_node = Node(
      package='ldlidar_stl_ros2',
      executable='ldlidar_stl_ros2_node',
      name='LD19',
      output='screen',
      parameters=[
        {'product_name': 'LDLiDAR_LD19'},
        {'topic_name': 'scan'},
        {'frame_id': 'laser_frame'},
        {'port_name': '/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0'},
        {'port_baudrate': 230400},
        {'laser_scan_dir': True},
        {'enable_angle_crop_func': False},
        {'angle_crop_min': 135.0},
        {'angle_crop_max': 225.0}
      ]
  )