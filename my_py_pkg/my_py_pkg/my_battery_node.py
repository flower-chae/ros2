#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_battery_interfaces.srv import SetLedInfo
from functools import partial


class MyBatteryNode(Node): 
    def __init__(self):
        super().__init__("my_battery_node")
        self.battery_timer_ = self.create_timer(4.0, self.battery_empty)
        self.log_timer_ = self.create_timer(1.0, self.log_status)
        self.battery_state_ = True

        self.led_set_client_ = self.create_client(SetLedInfo, "set_led") 

    def battery_empty(self):
        self.get_logger().info("battery is empty")
        self.battery_state_ = False

        request = SetLedInfo.Request()
        request.led_number =3
        request.state = True

        future = self.led_set_client_.call_async(request)
        future.add_done_callback(partial(self.callback_call_result,request=request))

                
        self.battery_timer_.cancel()
        self.battery_timer_ = self.create_timer(6.0, self.battery_full)


    def battery_full(self):
        self.get_logger().info("battery is full")
        self.battery_state_ = True

        request = SetLedInfo.Request()
        request.led_number =3
        request.state = False

        future = self.led_set_client_.call_async(request)
        future.add_done_callback(partial(self.callback_call_result,request=request))

        self.battery_timer_.cancel()
        self.battery_timer_ = self.create_timer(4.0, self.battery_empty)

    def log_status(self):
        self.get_logger().info("node is running")

    def callback_call_result(self, future, request):
        response = future.result()
        self.get_logger().info(f"led_number : {request.led_number}, request state : {request.state} => result is {response.success}")


        


def main(args=None):
    rclpy.init(args=args)
    node = MyBatteryNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

