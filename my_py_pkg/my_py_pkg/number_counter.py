#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool


class NumberCounterNode(Node): 
    def __init__(self):
        super().__init__("number_counter")
        self.counter_= 0
        self.number_count_publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.number_subscriber_ = self.create_subscription(Int64, "number", self.callback_number, 10)
        self.reset_counter_service_ = self.create_service(SetBool, "reset_counter", self.callback_reset_counter)
        self.get_logger().info("Number Counter has been started.")

    def callback_number(self, msg:Int64):
        self.counter_ += msg.data
        new_msg = Int64()
        new_msg.data = self.counter_
        self.number_count_publisher_.publish(new_msg)

    def callback_reset_counter(self, request:SetBool.Request, response:SetBool.Response):
        if request.data == True:
            self.counter_ = 0
            response.success = True
            response.message = "Counter has been reset"
            self.get_logger().info(f"request is : {request.data}, response success is : {response.success}, message is : {response.message}")
        else:
            response.success = False
            response.message = "Counter has not been reset"

        return response



def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

# my version, I tried timer hhh
#!/usr/bin/env python3
# import rclpy
# from rclpy.node import Node
# from example_interfaces.msg import UInt64


# class NumberSubPubNode(Node): 
#     def __init__(self):
#         super().__init__("number_sub_pub")
#         self.count = 0
#         self.publishers_=self.create_publisher(UInt64,"number_count", 10)
#         self.subscriber_=self.create_subscription(UInt64, "number",self.callback_int64_news, 10)
#         self.timer_ = self.create_timer(0.5, self.publish_number_count)
#         self.get_logger().info("Robot UInt64 sub/pub Station has been started.")

#     def publish_number_count(self):
#         msg = UInt64()
#         # TODO : add number
#         msg.data = self.count 
#         self.get_logger().info(f"data: {msg.data}")
#         self.publishers_.publish(msg)

#     def callback_int64_news(self, msg: UInt64):
#          self.count += msg.data



# def main(args=None):
#     rclpy.init(args=args)
#     node = NumberSubPubNode() 
#     rclpy.spin(node)
#     rclpy.shutdown()


# if __name__ == "__main__":
#     main()