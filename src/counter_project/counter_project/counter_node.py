#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class CounterNode(Node):
    def __init__(self):
        super().__init__('counter_node')
        self.publisher = self.create_publisher(Int64, '/count', 10)
        
        self.declare_parameter('publish_frequency', 1.0)
        freq = self.get_parameter('publish_frequency').value
        self.timer = self.create_timer(freq, self.timer_callback)
        
        # 声明参数，用于状态话题读取
        self.declare_parameter('counter_value', 0)
        
        self.counter = 0
        self.get_logger().info(f'✅ 计数器节点已启动，频率: {freq}秒')

    def timer_callback(self):
        # 发布计数
        msg = Int64()
        msg.data = self.counter
        self.publisher.publish(msg)
        self.get_logger().info(f'📤 发布计数: {self.counter}')
        
        # 同时更新参数服务器（供 status_publisher 读取）
        self.set_parameters([rclpy.parameter.Parameter(
            'counter_value',
            rclpy.Parameter.Type.INTEGER,
            self.counter
        )])
        
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = CounterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
