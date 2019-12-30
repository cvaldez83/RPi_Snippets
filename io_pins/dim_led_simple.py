
import RPi.GPIO as GPIO
import time

ledPIN = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPIN,GPIO.OUT)

steps_duty_cycle = 2

def dim():
	freq = 50
	red_led = GPIO.PWM(ledPIN,freq)
	red_led.start(0)
	pause_time = 0.010
	for i in range(0,100+1,steps_duty_cycle*3):
		red_led.ChangeDutyCycle(i)
		time.sleep(pause_time)
	time.sleep(.3)
	for i in range(100,-1,-steps_duty_cycle):
		red_led.ChangeDutyCycle(i)
		time.sleep(pause_time)
	#GPIO.cleanup()

for i in range(0,1):
	dim()
GPIO.cleanup()
