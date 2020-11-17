#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from datetime import datetime
import os
from random import randint
import threading
import signal

#
# Define GPIO# and mapping to the button name
btnMapping = {'22': 'btnP', '27': 'btnA', '17': 'btnB'}

#
# Maintain button status
# Use dictionary
statP, statA, statB = [], [], []
btnStatus = {'btnP': statP, 'btnA': statA, 'btnB': statB}

#
# Button press period list initial
listP, listA, listB = [], [], []
periodList = {'btnP': listP, 'btnA': listA, 'btnB': listB}

#
# Button press timeout
btnTimeout = 6

#
# Define SIGNAL handling


#
# GPIO button initial
GPIO.setmode(GPIO.BCM)
for item in btnMapping.keys():
    GPIO.setup(int(item), GPIO.IN)


def exportResult(btnName, pressPeriodSec, pressPeriodmSec):
    print("Button {} press interval is {:03d}.{:06d} seconds\n".format(
        btnName, pressPeriodSec, pressPeriodmSec))


def countDown(btnName, btnTimeout, btnSessionID):
    while btnTimeout > 0:
        time.sleep(1)
        btnTimeout -= 1
    if len(btnStatus.get(btnName)) > 0 and btnSessionID == btnStatus.get(btnName)[1]:
        # print("Button {} timeout, session ID: {}".format(btnName, btnSessionID))
        btnStatus.get(btnName).append('reset')
        # print(btnStatus.get(btnName), len(btnStatus.get(btnName)))
        exportResult(btnName, 6, 0)


def periodCalc(pin):
    '''
    Calculate time period between two button actions
    '''
    btnName = btnMapping.get(str(pin))
    btnTime = datetime.now()
    # print("The length of {} before appending is {}".format(btnName, len(periodList.get(btnName))))
    periodList.get(btnName).append(btnTime)
    # print("The length of {} after appending is {}".format(btnName, len(periodList.get(btnName))))
    #
    # Check if the button is reseted
    if len(btnStatus.get(btnName)) == 3:
        print("Ignore button {} action this time.\n".format(btnName))
        periodList.get(btnName).clear()
        btnStatus.get(btnName).clear()
    #
    #
    # If the button is pressed & released, calculate the period
    elif len(periodList.get(btnName)) == 2:
        diffSec = (periodList.get(btnName)[
                   1] - periodList.get(btnName)[0]).seconds
        diffmSec = (periodList.get(btnName)[
                    1] - periodList.get(btnName)[0]).microseconds
        exportResult(btnName, diffSec, diffmSec)
        periodList.get(btnName).clear()
        btnStatus.get(btnName).clear()
    else:
        btnStatus.get(btnName).append(1)
        btnSessionID = randint(65000, 65535)
        btnStatus.get(btnName).append(btnSessionID)
        #
        #
        # Start to button pressed countdown
        p = threading.Thread(target=countDown, args=(
            btnName, btnTimeout, btnSessionID,))
        p.start()
        print("Button {}, id {} is pressed and waiting for release.....".format(
            btnName, btnStatus.get(btnName)[1]))


#
# By real evaluating, long bouncetime cause button action not being detected easy (extreming condition)
for item in btnMapping.keys():
    GPIO.add_event_detect(int(item), GPIO.BOTH,
                          callback=periodCalc, bouncetime=1)

try:
    while True:
        # print('Waiting button to be pressed.....')
        time.sleep(32)
        print('Clear monitor after 2 second')
        time.sleep(2)
        os.system("clear")
except KeyboardInterrupt:
    pass
GPIO.cleanup()
