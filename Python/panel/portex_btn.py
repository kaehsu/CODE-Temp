#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

pBTNp = 22
aBTNp = 27
bBTNp = 17
listBTN = [pBTNp, aBTNp, bBTNp]

def event_occurredP(btn):
    return 'Button ' + str(btn) + ' is pressed.'

def event_occurredA(btn):
    return 'Button ' + str(btn) + ' is pressed.'

def event_occurredB(btn):
    return 'Button ' + str(btn) + ' is pressed.'


GPIO.setmode(GPIO.BCM)
for item in listBTN:
    GPIO.setup(item, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(pBTNp, GPIO.BOTH, callback=event_occurredP)
GPIO.add_event_detect(aBTNp, GPIO.BOTH, callback=event_occurredA)
GPIO.add_event_detect(bBTNp, GPIO.BOTH, callback=event_occurredB)

try:
    while True:
        print('Waiting button to be pressed.')
        time.sleep(86400)
except KeyboardInterrupt:
    print("Program is interrupted.")

GPIO.cleanup()

