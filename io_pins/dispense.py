#feed.py
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

GPIO.output(16, True)
time.sleep(.5)
GPIO.output(21, True)
time.sleep(.5)
GPIO.output(21, False)
GPIO.output(16,False)
