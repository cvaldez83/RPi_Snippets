# import RPi.GPIO as GPIO
import msvcrt
from msvcrt import getch
from time import sleep

freq = 1    # initial frequency
incr = .1   # desired frequency increment
pinSolenoid = 14 # RPi pin for solenoid control

# GPIO.setup(pinSolenoid,GPIO.OUT)

def cycleSolenoid(pin, freq):
    # GPIO.output(pin,True)
    print(f"GPIO pin {pin} set to True at frequency={freq}")
    sleep(1/freq)
    # GPIO.output(pin,False)
    print(f"GPIO pin {pin} set to False  at frequency={freq}")
    sleep(1/freq)


try:
    while True:
        print(freq)
        cycleSolenoid(pinSolenoid, freq)

        if msvcrt.kbhit():
            key = ord(getch()) #ord function turns getch() into an integer
            # print(key)
            if key == 27: #ESC
                print("Esc, exiting")
                GPIO.cleanup()
                break
            elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
                key = ord(getch())
                if key == 80: #Down arrow
                    freq -= incr
                    print(f"Decreasing frequency to {freq}")
                elif key == 72: #Up arrow
                    freq += incr
                    print(f"Increasing frequency to {freq}")
except KeyboardInterrupt:
        print("Keyboard Interrupt, exiting")
        GPIO.cleanup()