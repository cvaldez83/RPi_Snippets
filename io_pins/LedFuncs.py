
import RPi.GPIO as GPIO
import time

ledPIN = 12
GPIO.setwarnings(False)

def onoff():
	print('starting onoff function')
	print('ledPin = ' + str(ledPIN))
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(ledPIN, GPIO.OUT)
	print('outout: true')
	GPIO.output(ledPIN, True)
	time.sleep(5)
	print('output: false')
	GPIO.output(ledPIN, False)

def dim():
	print('starting dim function')
	steps_duty_cycle = 1
	sweep_range_dc = 10
	freq = 50
	pause_time = .5
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(ledPIN, GPIO.OUT)
	red_led = GPIO.PWM
	red_led = GPIO.PWM(ledPIN,freq)
	red_led.start(0)
	for i in range(0,sweep_range_dc+1,steps_duty_cycle):
		red_led.ChangeDutyCycle(i)
		print('DC: ' + str(i))
		time.sleep(pause_time)
	for i in range(sweep_range_dc,-1,-steps_duty_cycle):
		red_led.ChangeDutyCycle(i)
		print('DC: ' + str(i))
		time.sleep(pause_time)
	print('cleaning up')
	#red_led.ChangeDutyCycle(0)
	#red_led.stop()
	#GPIO.cleanup()

for i in range(0,1):
	onoff()
	time.sleep(3)
	dim()
	time.sleep(3)
	onoff()
