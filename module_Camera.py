import cv2
import struct
import pickle
import socket
import time

    
class Camera_frame_bytes():
	
	def __init__(self):
		self.encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),95]
		self.cam = cv2.VideoCapture(0)
		self.cam.set(3,320)
		self.cam.set(4,240)
		self.counter_Frame = 0
	
	def capture(self):
		self.rect,self.frame = self.cam.read()
		if self.rect: 
			self.counter_Frame += 1
			#self.frame = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)
			self.frame_bytes = cv2.flip(self.frame,0)
			self.result,self.frame = cv2.imencode('.jpg',self.frame,self.encode_param)
			self.frame_bytes = pickle.dumps(self.frame,0)
			self.frame_bytes_size = len(self.frame_bytes)
			#print('Frame Counter : {} ,Size : {}'.format(self.counter_Frame,self.frame_bytes_size))
			return struct.pack('>L',self.frame_bytes_size) + self.frame_bytes
			
			
			
	#def capture(self):
	'''Send frame by texture'''
		#self.rect,self.frame = self.cam.read()
		#print(self.frame.shape)
		#self.counter_Frame += 1
		#self.frame = cv2.flip(self.frame,0)
		#self.frame = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)
		#self.frame_bytes = self.frame.tostring()
		#self.frame_bytes_size = len(self.frame_bytes)
		#print('Frame Counter : {} ,Size : {}'.format(self.counter_Frame,self.frame_bytes_size))
		#return struct.pack('>L',self.frame_bytes_size) + self.frame_bytes		
		
			
camera_frame_bytes = Camera_frame_bytes()

			
			
			
			
			
			
			
			   
