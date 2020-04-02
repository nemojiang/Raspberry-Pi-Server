#!/usr/bin/python3
import time
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/Adafruit_SSD1306-1.6.2-py2.7.egg')
sys.path.append('/usr/local/lib/python2.7/dist-packages')
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
from threading import Thread
from DHT_11 import get_dht11_data
from DHT_11 import dht_11




def get_sys_info():
    cmd = "hostname -I | cut -d\' \' -f1"
    IP_Addr = 'IP Addr:' + subprocess.check_output(cmd, shell = True ).decode().replace('\n','')
    cmd = "top -bn1 | grep load | awk '{printf \"%.2f%%\", $(NF-2)}'"
    CPU_Load = 'CPU Load:' + subprocess.check_output(cmd, shell = True ).decode()
    cmd = "free -m | awk 'NR==2{printf \"%s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    Mem_Usage = 'Mem:' + subprocess.check_output(cmd, shell = True ).decode()
    cmd = "/opt/vc/bin/vcgencmd measure_temp"
    CPU_Temp = 'CPU Temp:' + subprocess.check_output(cmd,shell = True).decode().replace('\n','')[5:11]
    return IP_Addr,CPU_Temp,CPU_Load,Mem_Usage,dht_11.temp,dht_11.humidity

class Oled():
	def __init__(self):
		self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)
		self.image = Image.new('1',(self.disp.width,self.disp.height))
		self.draw = ImageDraw.Draw(self.image)
		self.font = ImageFont.load_default()
		self.disp.begin()
		self.disp.clear()
		self.disp.display()
	def draw_on_oled(self,content):
		self.draw.rectangle((0,0,self.disp.width,self.disp.height),outline = 0,fill = 0)
		y =4
		for item in content:
			self.draw.text((0,y),item,font = self.font,fill = 255)
			y+=10
		self.disp.image(self.image)
		self.disp.display()
	def clear(self):
		self.disp.clear()
		self.disp.display()

t_get_dht11_data = Thread(target = get_dht11_data,args = (dht_11,))		
t_get_dht11_data.start()		
oled = Oled()

