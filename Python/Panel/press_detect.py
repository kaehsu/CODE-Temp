#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from datetime import datetime
import os
import threading

#
# Define GPIO# and mapping button name
btnMapping = {'22': 'btnP', '27': 'btnA', '17': 'btnB'}

#
# Create button status
# Use list
# btnStatus = [0, 0, 0]
# Use dictionary
btnStatus = {'btnP': 0, 'btnA': 0, 'btnB': 0}

#
# Button period list initial
listP = []
listA = []
listB = []
periodList = {'btnP': listP, 'btnA': listA, 'btnB': listB}

#
# GPIO button initial
GPIO.setmode(GPIO.BCM)
for item in btnMapping.keys():
    GPIO.setup(int(item), GPIO.IN)


def calculate_period(btnName, btnTime):
    '''
    Calculate time period between two button actions
    '''
    print("The length of {} before appending is {}".format(
        btnName, len(periodList.get(btnName))))
    periodList.get(btnName).append(btnTime)
    print("The length of {} after appending is {}".format(
        btnName, len(periodList.get(btnName))))
    if len(periodList.get(btnName)) == 2:
        diffSec = (periodList.get(btnName)[
                   1] - periodList.get(btnName)[0]).seconds
        diffmSec = (periodList.get(btnName)[
                    1] - periodList.get(btnName)[0]).microseconds
        print("Button {} press interval is {}.{} seconds\n".format(
            btnName, diffSec, diffmSec))
        periodList.get(btnName).clear()
        btnStatus[btnName] = 0
    else:
        btnStatus[btnName] = 1


def event_occurred(pin):
    # GPIO.remove_event_detect(pin)
    # print('Button {} is pressed at {}.'.format(btnMapping.get(str(pin)), datetime.now()))
    # GPIO.add_event_detect(pin, GPIO.BOTH, callback = event_occurred, bouncetime = 300)
    calculate_period(btnMapping.get(str(pin)), datetime.now())


#
# By testing, long bouncetime(>=2ms) will cause button action not being detected (extreming condition)
for item in btnMapping.keys():
    GPIO.add_event_detect(int(item), GPIO.BOTH,
                          callback=event_occurred, bouncetime=1)

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
