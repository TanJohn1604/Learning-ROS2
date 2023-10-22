#!/usr/bin/env python3 
import rclpy 
from rclpy.node import Node 

from ros2_user_pkg.srv import ImageService
import cv2
from cv_bridge import CvBridge

class ImageServer(Node):
	def __init__(self):
		super().__init__('camera_server')
		self.srv = self.create_service(ImageService, 'image_service', self.rotate_angle)

	def rotate_angle(self, request, response): 		
		if request.request_angle > 0 and request.request_angle < 90:
			image = cv2.imread('/home/tan/Documents/workspace/ROS2_py_ws/src/ros2_user_pkg/img/image2.jpg')
			image_msg = CvBridge().cv2_to_imgmsg(image)
			response.response_image = image_msg
		else:
			image = cv2.imread('/home/tan/Documents/workspace/ROS2_py_ws/src/ros2_user_pkg/img/image2.jpg')
			image_msg = CvBridge().cv2_to_imgmsg(image)
			response.response_image = image_msg
		return response



def main(args=None):
	rclpy.init()
	server_node = ImageServer()
	print("Image Server Running...")
	

	try:
		rclpy.spin(server_node)
	except KeyboardInterrupt:
		print("Terminating Node...")
		server_node.destroy_node()


if __name__ == '__main__':
	main()