#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String, Float32

wheel = 10.0

class RpmPublisher(Node):
	def __init__(self):
		super().__init__("rpm_node")
		self.declare_parameter("wheel_r",wheel)
		self.pub = self.create_publisher(Float32, "rpm", 10)
		self.timer = self.create_timer(0.5, self.RpmPublish)
		self.counter = 0
	def RpmPublish(self):
		rpm = Float32()
		rpm.data = self.get_parameter("wheel_r").get_parameter_value().double_value
		self.pub.publish(rpm)


def main(args=None):
	rclpy.init()
	my_pub = RpmPublisher()
	print("RPM Node Running...")

	try:
		rclpy.spin(my_pub)
	except KeyboardInterrupt:
		print("Terminating Node...")
		my_pub.destroy_node()


if __name__ == '__main__':
	main()