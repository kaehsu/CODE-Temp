
import RPi.GPIO as GPIO
import time
from random import randint

pinYLED = 13
pinWLED = 6
pinGLED = 19
pinBLED = 5
pinRLED = 26
totalPin = (5, 6, 13, 19, 26)


GPIO.setmode(GPIO.BCM)
GPIO.setup(pinYLED, GPIO.OUT)
GPIO.setup(pinWLED, GPIO.OUT)
GPIO.setup(pinGLED, GPIO.OUT)
GPIO.setup(pinBLED, GPIO.OUT)
GPIO.setup(pinRLED, GPIO.OUT)

try:
    while True:
        rn = randint(0, 4)
        randGPIO = totalPin[rn]
        GPIO.output(randGPIO, 1)
        time.sleep(0.1)
        GPIO.output(randGPIO, 0)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
    GPIO.cleanup()
