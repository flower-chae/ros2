#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/u_int64.hpp"
#include <cinttypes>

using namespace std::chrono_literals;
using namespace std::placeholders;

class NumberSubPubNode : public rclcpp::Node 
{
public:
    NumberSubPubNode() : Node("number_sub_pub") 
    {
        publisher_=this->create_publisher<example_interfaces::msg::UInt64>("number_count",10);
        subscriber_= this->create_subscription<example_interfaces::msg::UInt64>("number", 10, std::bind(&NumberSubPubNode::callback_int64_news, this, _1));
        timer_ = this->create_wall_timer(0.5s, std::bind(&NumberSubPubNode::publish_number_count, this));

        RCLCPP_INFO(this->get_logger(), "Robot Uint64 sub/pub Station has been started");

    }

private:
    rclcpp::Publisher<example_interfaces::msg::UInt64>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Subscription<example_interfaces::msg::UInt64>::SharedPtr subscriber_;
    uint64_t count = 0;
    
    void publish_number_count()
    {
        auto msg = example_interfaces::msg::UInt64();
        msg.data = count;
        RCLCPP_INFO(this->get_logger(),"data %" PRIu64,msg.data);
        publisher_->publish(msg);
    }
    void callback_int64_news(const example_interfaces::msg::UInt64::SharedPtr msg)
    {
        count += msg->data;
    }



};


// publisher_ = this->create_publisher<example_interfaces::msg::UInt64>("number", 10);
//         timer_=this->create_wall_timer(0.5s, std::bind(&NumberStationNode::publish_number, this));
//         RCLCPP_INFO(this->get_logger(), "Robot Uint64 Station has been started");

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberSubPubNode>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}



// rclcpp::Publisher<example_interfaces::msg::UInt64>::SharedPtr publisher_;
//     rclcpp::TimerBase::SharedPtr timer_;