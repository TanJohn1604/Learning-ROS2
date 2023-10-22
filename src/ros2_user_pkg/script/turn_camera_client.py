#!/usr/bin/env python3 
import rclpy 
from rclpy.node import Node 
import cv2
from cv_bridge import CvBridge
from ros2_user_pkg.srv import ImageService


class ImageClient(Node):
	def __init__(self):
		super().__init__('camera_client')
		self.client = self.create_client(ImageService, 'image_service')
		self.req = ImageService.Request()

	def send_request(self, num):
		self.req.request_angle = int(num)
		self.client.wait_for_service()
		self.future = self.client.call_async(self.req)
		rclpy.spin_until_future_complete(self, self.future)

		self.result = self.future.result()
		return self.result 
		

def main(args=None):
	rclpy.init()
	client_node = ImageClient()
	print("Image Client Running...")

	try:
		user_input = input("Enter an integer: ")
		res = client_node.send_request(user_input)
		image = CvBridge().imgmsg_to_cv2(res.response_image)
		cv2.imshow("camera",image)
		print("image is captured")
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	except KeyboardInterrupt:
		print("Terminating Node...")
		client_node.destroy_node()


if __name__ == '__main__':
	main()