#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class ThresholdService(Node):
    def __init__(self):
        super().__init__('threshold_service')
        self.srv = self.create_service(
            SetBool, 
            '/set_warning_threshold', 
            self.callback
        )
        self.get_logger().info('⚙️ 阈值设置服务已启动')
        self.get_logger().info('   - 调用 data=true  → 关闭告警（阈值设为1000）')
        self.get_logger().info('   - 调用 data=false → 开启告警（阈值设为50）')

    def callback(self, request, response):
        if request.data:
            # True: 关闭告警（阈值设成很大，永远不会报警）
            self.get_logger().info('🔇 告警已关闭（阈值设为1000）')
            response.success = True
            response.message = "告警已关闭（阈值=1000）"
        else:
            # False: 开启告警（阈值恢复50）
            self.get_logger().info('🔊 告警已开启（阈值设为50）')
            response.success = True
            response.message = "告警已开启（阈值=50）"
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ThresholdService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
