import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_LED = range(0,19)
for pin in pin_LED:
	GPIO.cleanup()
	time.sleep(.01)
	
