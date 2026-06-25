#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int64
import time

class StatusPublisher(Node):
    def __init__(self):
        super().__init__('status_publisher')
        self.publisher = self.create_publisher(String, '/counter_status', 10)
        # 直接订阅 /count 话题获取计数值
        self.subscription = self.create_subscription(
            Int64, '/count', self.count_callback, 10
        )
        self.timer = self.create_timer(5.0, self.timer_callback)
        self.start_time = time.time()
        self.counter_value = 0
        self.has_received = False
        self.get_logger().info('📊 状态发布节点已启动 (每5秒发布一次)')

    def count_callback(self, msg):
        self.counter_value = msg.data
        self.has_received = True

    def timer_callback(self):
        if not self.has_received:
            return
        run_time = int(time.time() - self.start_time)
        msg = String()
        msg.data = f'当前计数: {self.counter_value}, 运行时间: {run_time}秒'
        self.publisher.publish(msg)
        self.get_logger().info(f'📊 {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = StatusPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
# 维护者: freerft4
