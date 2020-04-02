import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Wheel():
	def __init__(self,pin_Ena,pin_A,pin_B):
		self.pin_Ena = pin_Ena
		self.pin_A = pin_A
		self.pin_B = pin_B
		self.speed = 100
		for pin in (self.pin_Ena,self.pin_A,self.pin_B):
			GPIO.setup(pin,GPIO.OUT)
		self.pwm = GPIO.PWM(self.pin_Ena,200)
		self.pwm.start(0)
	def motor_Forward(self,speed):
		GPIO.output(self.pin_A,GPIO.LOW)
		GPIO.output(self.pin_B,GPIO.HIGH)
		self.pwm.ChangeDutyCycle(speed)
	def motor_Backward(self,speed):
		GPIO.output(self.pin_A,GPIO.HIGH)
		GPIO.output(self.pin_B,GPIO.LOW)
		self.pwm.ChangeDutyCycle(speed)
	def motor_Stop(self):
		GPIO.output(self.pin_A,GPIO.HIGH)
		GPIO.output(self.pin_B,GPIO.HIGH)
		
wheel_L = Wheel(26,13,19)
wheel_R = Wheel(21,16,20)

class Drive():
	def __init__(self,wheel_L,wheel_R):
		self.wheel_L = wheel_L
		self.wheel_R = wheel_R
		GPIO.setup(12,GPIO.IN)
	def forward(self):
		self.wheel_L.motor_Forward(self.wheel_L.speed)
		self.wheel_R.motor_Forward(self.wheel_R.speed)
	def backward(self):
		self.wheel_L.motor_Backward(self.wheel_L.speed)
		self.wheel_R.motor_Backward(self.wheel_R.speed)
	def left(self):
		self.wheel_L.motor_Forward(0)
		self.wheel_R.motor_Forward(100)
	def right(self):
		self.wheel_L.motor_Forward(100)
		self.wheel_R.motor_Forward(0)
	def stop(self):
		self.wheel_L.motor_Stop()
		self.wheel_R.motor_Stop()
		#print('test')
	def end(self):
		GPIO.cleanup()
	def change_Speed(self,slider_Value):
		self.wheel_L.speed = slider_Value
		self.wheel_R.speed = slider_Value
		
	def infrared_break(self):
		return GPIO.input(12)
		
		
drive = Drive(wheel_L,wheel_R)
		

		
