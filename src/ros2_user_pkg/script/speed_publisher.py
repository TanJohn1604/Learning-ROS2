#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String, Float32


class Speed(Node):
	def __init__(self):
		super().__init__("speed_node")
		self.sub = self.create_subscription(Float32, "rpm", self.subscriber_callback, 10)
		self.pub = self.create_publisher(Float32, "speed", 10)
	def subscriber_callback(self, msg):
		
		speed_rpm = Float32()
		speed_rpm.data = msg.data / 3
		self.pub.publish(speed_rpm)


def main(args=None):
	rclpy.init()
	my_sub = Speed()
	print("Waiting for rpm ")

	try:
		rclpy.spin(my_sub)
	except KeyboardInterrupt:
		print("Terminating Node...")
		my_sub.destroy_node()


if __name__ == '__main__':
	main()