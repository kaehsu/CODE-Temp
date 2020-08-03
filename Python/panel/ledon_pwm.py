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


try:
    while True:
        color, freq = input(
            'Please enter the color(g, r, b, y, o) and frequency:')
        if color in (g, r, b, y, o):

except KeyboardInterrupt:
    print('Program exit!')
    GPIO.cleanup()
