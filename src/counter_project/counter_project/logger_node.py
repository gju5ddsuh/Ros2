#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from datetime import datetime
import sys

class LoggerNode(Node):
    def __init__(self):
        super().__init__('logger_node')
        
        self.sub_count = self.create_subscription(
            Int64, '/count', self.count_callback, 10
        )
        self.sub_square = self.create_subscription(
            Int64, '/square', self.square_callback, 10
        )
        
        self.count_value = 0
        self.square_value = 0
        self.count_received = False
        self.square_received = False
        
        self.declare_parameter('warning_threshold', 50)
        self.get_logger().info('📋 日志节点已启动')

    def count_callback(self, msg):
        self.count_value = msg.data
        self.count_received = True
        self.try_print_log()

    def square_callback(self, msg):
        self.square_value = msg.data
        self.square_received = True
        self.try_print_log()

    def try_print_log(self):
        if self.count_received and self.square_received:
            time_str = datetime.now().strftime('%H:%M:%S')
            threshold = self.get_parameter('warning_threshold').value
            
            # 强制实时输出
            if self.square_value > threshold:
                print(f'\033[91m📋 [{time_str}] 计数: {self.count_value:3d}, 平方: {self.square_value:5d}  🚨 警告！\033[0m', flush=True)
            else:
                print(f'📋 [{time_str}] 计数: {self.count_value:3d}, 平方: {self.square_value:5d}', flush=True)
            
            self.count_received = False
            self.square_received = False

def main(args=None):
    rclpy.init(args=args)
    node = LoggerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
