#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_battery_interfaces.msg import LedPanelState
from my_battery_interfaces.srv import SetLedInfo


class MyPanelNode(Node): 
    def __init__(self):
        super().__init__("my_panel")
        self.panel = [0,0,0]
        self.panel_publisher_ = self.create_publisher(LedPanelState, "led_panel_state", 10)
        self.panel_timer_ = self.create_timer(1.0, self.publish_led_state)
        self.led_set_service_ = self.create_service(SetLedInfo, "set_led", self.callback_set_led)

    def publish_led_state(self):
        msg = LedPanelState()
        msg.data = self.panel
        self.panel_publisher_.publish(msg)


    def callback_set_led(self, request:SetLedInfo.Request, response:SetLedInfo.Response):
        if request.led_number == 3 and request.state == True:
            self.get_logger().info("callback : led on")
            self.panel[2] = 1
            response.success = True
        elif request.led_number == 3 and request.state == False:
            self.get_logger().info("callback : led off")
            self.panel[2] = 0
            response.success = True

        else:
            response.success = False

        return response




def main(args=None):
    rclpy.init(args=args)
    node = MyPanelNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()