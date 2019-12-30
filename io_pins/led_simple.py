import RPi.GPIO as GPIO
import time

pinLED = 12
on_time = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED, GPIO.OUT)
GPIO.setwarnings(False)

GPIO.output(pinLED, True)
time.sleep(on_time)
GPIO.output(pinLED, False)


