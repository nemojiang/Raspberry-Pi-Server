import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Rgb():
    def __init__(self):
        GPIO.setup(8,GPIO.OUT)
        GPIO.setup(25,GPIO.OUT)
        GPIO.setup(7,GPIO.OUT)
              
    def led_Red(self):
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(25,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        
    def led_Green(self):
        GPIO.output(8,GPIO.LOW)
        GPIO.output(25,GPIO.HIGH)
        GPIO.output(7,GPIO.LOW)
        
    def led_Blue(self):
        GPIO.output(8,GPIO.LOW)
        GPIO.output(25,GPIO.LOW)
        GPIO.output(7,GPIO.HIGH)
        
    def led_White(self):
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(25,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)
        
    def led_off(self):
        GPIO.output(8,GPIO.LOW)
        GPIO.output(25,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
              
    def end(self):
        GPIO.cleanup()

led = Rgb()
        


		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
