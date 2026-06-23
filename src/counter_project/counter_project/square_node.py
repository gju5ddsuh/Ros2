#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class SquareNode(Node):
    def __init__(self):
        super().__init__('square_node')
        self.subscription = self.create_subscription(Int64, '/count', self.callback, 10)
        self.publisher = self.create_publisher(Int64, '/square', 10)
        self.get_logger().info('平方计算节点已启动')

    def callback(self, msg):
        result = msg.data * msg.data
        self.publisher.publish(Int64(data=result))
        self.get_logger().info(f'🔢 {msg.data}² = {result}')

def main(args=None):
    rclpy.init(args=args)
    node = SquareNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
