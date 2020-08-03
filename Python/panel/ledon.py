#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from random import randint

pinGLED = 19
pinRLED = 26
pinBLED = 5
pinYLED = 13
pinOLED = 6
totalPin = (pinGLED, pinRLED, pinBLED, pinYLED, pinOLED)

namePin = {
    '13': 'Yellow LED',
    '6': 'Orange LED',
    '19': 'Green LED',
    '5': 'Blue LED',
    '26': 'Red LED',
}

if GPIO.getmode(pinGLED):
    GPIO.cleanup

GPIO.setmode(GPIO.BCM)
for pin in totalPin:
    GPIO.setup(pin, GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)
    GPIO.PWM(pin, 50)


try:
    while True:
        rnA = randint(0, 4)
        # print('Now the magic number is {}!'.format(rnA))
        nGPIO = totalPin[rnA]
        nameLED = namePin[str(nGPIO)]
        # print('Now the magic GPIO is {}!'.format(nGPIO))
        rnB = randint(rnA+1, 10)
        print('Will light {} {} times'.format(nameLED, rnB))
        time.sleep(1)
        for c in range(1, rnB+1):
            GPIO.output(nGPIO, GPIO.HIGH)  # LED On
            time.sleep(0.1)
            GPIO.output(nGPIO, GPIO.LOW)  # LED Off
            time.sleep(0.1)
except KeyboardInterrupt:
    print('Program exit!')
    pass
    GPIO.cleanup()
