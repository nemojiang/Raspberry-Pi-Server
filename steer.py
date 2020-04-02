import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Steer():
	def __init__(self,pin):
		GPIO.setup(pin,GPIO.OUT)
		self.pwm = GPIO.PWM(pin,50)
		self.pwm.start(0)
		
	def turn(self,angle):
		self.pwm.ChangeDutyCycle(angle)
		time.sleep(.2)
		self.pwm.ChangeDutyCycle(0)
		time.sleep(.2)
		
		
camera_pan = Steer(18)
camera_tilt = Steer(23)
led_pan = Steer(4)



if __name__ == '__main__':
	import time
	import RPi.GPIO as GPIO
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

