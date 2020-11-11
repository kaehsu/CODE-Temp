#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from datetime import datetime
import os

#
# Define GPIO# and mapping button name
btnMapping = {'22': 'btnP', '27': 'btnA', '17': 'btnB'}

#
# GPIO button initial
GPIO.setmode(GPIO.BCM)
for item in btnMapping.keys():
    GPIO.setup(int(item), GPIO.IN)

#
# Button period list initial
listP = []
listA = []
listB = []
periodList = {'btnP': listP, 'btnA': listA, 'btnB': listB}


def calculate_period(btnName, btnTime):
    periodList.get(btnName).append(btnTime)
    if len(periodList.get(btnName)) == 2:
        print("Button {} press interval is {}".format(
            btnName, (periodList.get(btnName)[1] - periodList.get(btnName)[0]).seconds))
        periodList.get(btnName).clear()


def event_occurred(pin):
    # GPIO.remove_event_detect(pin)
    # print('Button {} is pressed at {}.'.format(btnMapping.get(str(pin)), datetime.now()))
    # GPIO.add_event_detect(pin, GPIO.BOTH, callback = event_occurred, bouncetime = 300)
    calculate_period(btnMapping.get(str(pin)), datetime.now())


for item in btnMapping.keys():
    GPIO.add_event_detect(
        int(item), GPIO.BOTH, callback=event_occurred, bouncetime=32)

try:
    while True:
        # print('Waiting button to be pressed.....')
        time.sleep(32)
        print('Clear monitor after 2 second')
        time.sleep(2)
        os.system("clear")
        pass
except KeyboardInterrupt:
    pass
GPIO.cleanup()
