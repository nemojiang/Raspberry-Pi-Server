#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
from threading import Thread

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Dht_11():
	
	def __init__(self):
		self.temp = ''
		self.humidity = ''
	
	def rpi_connect_dht11(self):
		self.bin_list=[]
		self.dec_list=[]
		bin_list_count = 0
		time.sleep(1)
		
		GPIO.setup(5,GPIO.OUT)
		GPIO.output(5,GPIO.LOW)
		time.sleep(0.02)
		GPIO.output(5,GPIO.HIGH)
		
		GPIO.setup(5,GPIO.IN)		
		while GPIO.input(5) == GPIO.LOW:
			continue
		while GPIO.input(5) == GPIO.HIGH:
			continue
		while bin_list_count < 40:
			high_duration=0
			while GPIO.input(5) == GPIO.LOW:
				continue
			while GPIO.input(5) == GPIO.HIGH:
				high_duration+=1
				if high_duration >100:break
			if high_duration > 8:
				self.bin_list.append(1)
			else:
				self.bin_list.append(0)
			bin_list_count+=1
		
	
	def bin_To_dec(self):
		n=0
		while n < 40:
			temp=map(str,self.bin_list[n:n+8])
			temp=''.join(temp)
			temp=int(temp,2)
			self.dec_list.append(temp)
			n+=8
	def check(self):
		if self.dec_list[0] + self.dec_list[1] + self.dec_list[2] + self.dec_list[3] == self.dec_list[-1]:
			self.humidity = 'Humidity : '+ str(self.dec_list[0]) +' %'
			self.temp = 'Temp : '+ str(self.dec_list[2]*9/5+32) +' F'
			
			
def get_dht11_data(dht_11):
	while True:
		dht_11.rpi_connect_dht11()
		dht_11.bin_To_dec()
		dht_11.check()
		#print(dht_11.temp,dht_11.humidity)
		time.sleep(5)
	
dht_11 = Dht_11()

		
