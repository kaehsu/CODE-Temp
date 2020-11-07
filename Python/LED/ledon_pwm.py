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

gLEDp = GPIO.PWM(pinGLED, 1)
rLEDp = GPIO.PWM(pinRLED, 1)
bLEDp = GPIO.PWM(pinBLED, 1)
yLEDp = GPIO.PWM(pinYLED, 1)
oLEDp = GPIO.PWM(pinOLED, 1)
allLEDp = [gLEDp, rLEDp, bLEDp, yLEDp, oLEDp]

for item in allLEDp:
    item.start(100)

try: 
    while True:
        for item in allLEDp:
            rNf = randint(1, 100)/10
            rNd = randint(0, 100)
            item.ChangeFrequency(rNf)
            item.ChangeDutyCycle(rNd)
        time.sleep(1)

except KeyboardInterrupt:
    print('Program exit!')
    for item in allLEDp:
        item.stop()
    GPIO.cleanup()


