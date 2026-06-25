#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty
import subprocess

class ResetService(Node):
    def __init__(self):
        super().__init__('reset_service')
        self.srv = self.create_service(Empty, '/reset_counter', self.reset_callback)
        self.get_logger().info('🔄 重置服务已启动')

    def reset_callback(self, request, response):
        self.get_logger().info('⏳ 正在重置计数器...')
        subprocess.run(['pkill', '-f', 'counter_node'], check=False)
        self.get_logger().info('✅ 计数器已重置为0')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ResetService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    
# 维护者: 159357gwj
# 维护者: 159357gwj
