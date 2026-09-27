
#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

using namespace std::chrono_literals;

class NumberPublisherNode : public rclcpp::Node
{
public:
    NumberPublisherNode() : Node("number_publisher"), number_(2)
    {
        number_publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number", 10);
        number_timer_ = this->create_wall_timer(1s,
                                                std::bind(&NumberPublisherNode::publishNumber, this));
        RCLCPP_INFO(this->get_logger(), "Number publisher has been started.");
    }

private:
    void publishNumber()
    {
        auto msg = example_interfaces::msg::Int64();
        msg.data = number_;
        number_publisher_->publish(msg);
    }

    int number_;
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr number_publisher_;
    rclcpp::TimerBase::SharedPtr number_timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberPublisherNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}



// It's my code
// #include "rclcpp/rclcpp.hpp"
// #include "example_interfaces/msg/u_int64.hpp"


// using namespace std::chrono_literals;
// // timer_=this->create_wall_timer(0.5s, std::bind(&RobotNewsStationNode::publishNews, this));
// class NumberStationNode : public rclcpp::Node 
// {
// public:
//     NumberStationNode() : Node("number_station") 
//     {
//         publisher_ = this->create_publisher<example_interfaces::msg::UInt64>("number", 10);
//         timer_=this->create_wall_timer(0.5s, std::bind(&NumberStationNode::publish_number, this));
//         RCLCPP_INFO(this->get_logger(), "Robot Uint64 Station has been started");

//     }

// private:
//     rclcpp::Publisher<example_interfaces::msg::UInt64>::SharedPtr publisher_;
//     rclcpp::TimerBase::SharedPtr timer_;
//     void publish_number()
//     {
//         auto msg = example_interfaces::msg::UInt64();
//         msg.data = 2;
//         publisher_->publish(msg);

//     }
// };

// int main(int argc, char **argv)
// {
//     rclcpp::init(argc, argv);
//     auto node = std::make_shared<NumberStationNode>(); 
//     rclcpp::spin(node);
//     rclcpp::shutdown();
//     return 0;
// }