#!/usr/bin/python3
from threading import Thread
import socket
import time
from drive import drive
from sys_info import get_sys_info
from sys_info import oled
from steer import camera_pan,camera_tilt,led_pan
from RGB import led
from module_Camera import camera_frame_bytes


def build_Server():
	global server
	oled.draw_on_oled(('\n\n-----POWER ON-----',))
	time.sleep(2)
	try:
		server = socket.socket()
		server.bind(('192.168.0.142',6988))
		#server.bind(('192.168.43.119',6970))
	except Exception as e:
		print(e)
		oled.draw_on_oled(('\n\n--IP Bind Error--',))
		time.sleep(2)
	else:	
		server.listen(5)

def live_update_sys_info():
	while connect_status:
		if drive.infrared_break() == False:
			#print('break')
			drive.stop()
		#print('live_update_sys_info {}'.format(connect_status))
		sys_data = get_sys_info()
		print(sys_data)
		sys_info.send(','.join(sys_data).encode())
		oled.draw_on_oled(sys_data)
		time.sleep(1)

def get_steer_angle():
	while connect_status:
		#print('get_steer_angel {}'.format(connect_status))
		command_steer = steers.recv(3).decode()
		if not command_steer : break
		print(command_steer)
		steer = command_steer[0]
		angle = int(command_steer[1:])
		if steer == 'a':
			camera_pan.turn(angle)
		if steer == 'b':
			camera_tilt.turn(angle)
		if steer == 'c':
			led_pan.turn(angle)


def get_leds_status():
	while connect_status:
		#print('get_leds_status {}'.format(connect_status))
		command_led = leds.recv(2).decode()
		if not command_led: break
		print(command_led)
		if command_led[1] == 'T':
			if command_led[0] == 'r':
				led.led_Red()
			if command_led[0] == 'g':
				led.led_Green()
			if command_led[0] == 'b':
				led.led_Blue()
			if command_led[0] == 'w':
				led.led_White()
		else:
			led.led_off()
		
def send_camera_frame_bytes():
	while connect_status:
		#print('send_camera_frame_bytes {}'.format(connect_status))
		data = camera_frame_bytes.capture()
		camera.sendall(data)
		respone = camera.recv(1) 
		#time.sleep(.1)
		
		
def server_init():
		global conn,sys_info,steers,leds,camera,connect_status
		#try:
			#print(connect_status)
		#except Exception as e:
			#print(e)
		oled.draw_on_oled(('\n\n-----Waitting-----',))
		conn,(host,port) = server.accept()
		#oled.draw_on_oled(('\n\n------Control-----',))
		#time.sleep(1)
		sys_info,(host,port) = server.accept()
		#print('1st while {}'.format(connect_status))
		#oled.draw_on_oled(('\n\n-----Sys_Info-----',))
		#time.sleep(1)
		steers,(host,port) = server.accept()
		#oled.draw_on_oled(('\n\n-----Steers-----',))
		#time.sleep(1)
		leds,(host,port) = server.accept()
		#oled.draw_on_oled(('\n\n-----RGB_Leds-----',))
		#time.sleep(1)
		camera,(host,port) = server.accept()
		#oled.draw_on_oled(('\n\n----Camera----'))
		connect_status = True
		print(id(connect_status),'#################################')
		oled.draw_on_oled(('\n\n-----Connected-----',))
		#time.sleep(1)
		t_oled_client = Thread(target = live_update_sys_info)
		t_oled_client.start()
		t_steers = Thread(target = get_steer_angle)
		t_steers.start()
		t_leds = Thread(target = get_leds_status)
		t_leds.start()
		t_send_camera_frame_bytes = Thread(target = send_camera_frame_bytes)
		t_send_camera_frame_bytes.start()
		#print('Client Connected.') 
	
		
def processing():
	global connect_status
	while True:
		server_init()
		while True:
			command_Control = conn.recv(1).decode()
			if not command_Control:break
			
			if command_Control in ['w','s','l','r','p','q']:
				if command_Control == 'w':
					print('w')
					drive.forward()
			
				elif command_Control == 's':
					print('s')
					drive.backward()
		
				elif command_Control == 'l':
					print('l')
					drive.left()
		
				elif command_Control == 'r':
					print('r')
					drive.right()
			
				elif command_Control == 'p':
					print('p') 
					drive.stop()
					
				elif command_Control == 'q':
					connect_status = False
					print(id(connect_status),'###############')
					#sys_info.shutdown(2)
					#sys_info.close()
					led.led_off()
					oled.clear()
					print('q')
					break
					
					
			#elif command_Control in ['q','i']:
				#if command_Control == 'q':
					#print('q')
					#led.led_off()
					#connect_status = False
					#oled.clear()
					##print('i{}'.format(connect_status))
					#break

			else:
				slider_Value = int(command_Control) * 10
				if slider_Value == 90:
					slider_Value = 100
				drive.change_Speed(slider_Value)
				print(drive.wheel_L.speed,drive.wheel_R.speed)
			

		
if __name__ == '__main__':
	time.sleep(2)
	build_Server()
	processing()

		
		
