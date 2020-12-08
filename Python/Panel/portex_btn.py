#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from datetime import datetime
import os
from random import randint
import threading
import signal
import argparse
from portex_exec import execCMD

#
# Command line argument
parser = argparse.ArgumentParser(
    description='PORTEX Panel Program for Panel Button')
parser.add_argument('-b', '--bouncetime', type=int,
                    help='GPIO bouncetime in milliseconds, range 1ms to 512ms, default 64ms', default=64)
parser.add_argument('-t', '--timeout', type=int,
                    help='Button press timeout in seconds, range 2s to 16s, default 6s', default=6)
cargs = parser.parse_args()

#
# Input GPIO bouncetime check
# By serial testing, GPIO bouncetime should less than 512ms
if 1 <= cargs.bouncetime <= 512:
    gpioBouncetime = cargs.bouncetime
    # print('Button GPIO bouncetime is {}ms.'.format(gpioBouncetime))
else:
    # print('Out of suggestted bouncetime range, change bouncetime to default {} ms.'.format(64))
    gpioBouncetime = 64

#
# Input button timeout check, maximun timeout is set to 16 seconds
# Default is 6 seconds,
if 2 <= cargs.timeout <= 16:
    cbtnTimeout = cargs.timeout
    # print('Button timeout is {} second(S)'.format(cbtnTimeout))
else:
    cbtnTimeout = 6
    # print('Out of suggestted timeout range, change timeout to default {} seconds.'.format(cbtnTimeout))


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
# GPIO button initial
GPIO.setmode(GPIO.BCM)
for item in btnMapping.keys():
    GPIO.setup(int(item), GPIO.IN)


def exportResult(btnName, pressPeriodSec, pressPeriodmSec):
    '''
    Export button action result.
    '''
    print("Button {} press interval is {:03d}.{:06d} seconds\n".format(
        btnName, pressPeriodSec, pressPeriodmSec))


def countDown(btnName, btnTimeout, btnSessionID):
    '''
    Each time a button is pressed, a timer will start to countdown for button timeout.
    '''
    while btnTimeout > 0:
        time.sleep(1)
        btnTimeout -= 1
    if len(btnStatus.get(btnName)) > 0 and btnSessionID == btnStatus.get(btnName)[1]:
        # print("Button {} timeout, session ID: {}".format(btnName, btnSessionID))
        btnStatus.get(btnName).append('reset')
        # print(btnStatus.get(btnName), len(btnStatus.get(btnName)))
        # exportResult(btnName, cbtnTimeout, 0)
        execCMD(btnName, cbtnTimeout)


def periodCalc(pin):
    '''
    Calculate time period between two button actions.
    '''
    btnName = btnMapping.get(str(pin))
    btnTime = datetime.now()
    # print("The length of {} before appending is {}".format(btnName, len(periodList.get(btnName))))
    periodList.get(btnName).append(btnTime)
    # print("The length of {} after appending is {}".format(btnName, len(periodList.get(btnName))))
    #
    # Check if the button is reseted
    if len(btnStatus.get(btnName)) == 3:
        # print("Ignore button {} action this time.\n".format(btnName))
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
        # exportResult(btnName, diffSec, diffmSec)
        execCMD(btnName, diffSec+diffmSec/1000000)
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
            btnName, cbtnTimeout, btnSessionID,))
        p.start()
        # print("Button {}, id {} is pressed and waiting for release.....".format(btnName, btnStatus.get(btnName)[1]))


def hangUP(signum, frame):
    GPIO.cleanup()
    exit()


def kbInterrupt(signum, frame):
    GPIO.cleanup()
    raise KeyboardInterrupt()


#
# By real evaluating, long bouncetime cause button action not being detected easy (extreming condition)
for item in btnMapping.keys():
    GPIO.add_event_detect(int(item), GPIO.BOTH,
                          callback=periodCalc, bouncetime=gpioBouncetime)

signal.signal(signal.SIGHUP, hangUP)
signal.signal(signal.SIGINT, kbInterrupt)

try:
    while True:
        # print('Waiting button to be pressed.....')
        # time.sleep(32)
        # print('Clear monitor after 2 seconds')
        # time.sleep(2)
        # os.system("clear")
        pass
except KeyboardInterrupt:
    pass
