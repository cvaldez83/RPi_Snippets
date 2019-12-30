#blink.py
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#light pin = 16
GPIO.setup(16, GPIO.OUT)

GPIO.output(16, True)
time.sleep(.5)
GPIO.output(16,False)