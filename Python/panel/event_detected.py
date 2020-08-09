#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from datetime import datetime

pBTNp = 22
aBTNp = 27
bBTNp = 17
allBTNp = [pBTNp, aBTNp, bBTNp]

GPIO.setmode(GPIO.BCM)
for item in allBTNp:
    GPIO.setup(item, GPIO.IN)

# GPIO.setup(pBTNp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(aBTNp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(bBTNp, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def event_occurred(pin):
    GPIO.remove_event_detect(pin)
    print('Button {} is pressed at {}.'.format(pin, datetime.now()))
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=event_occurred, bouncetime=1000)

for item in allBTNp:
    GPIO.add_event_detect(item, GPIO.BOTH, callback=event_occurred, bouncetime=1000)
# GPIO.add_event_detect(pBTNp, GPIO.FALLING, callback=event_occurred, bouncetime=1000)
# GPIO.add_event_detect(aBTNp, GPIO.FALLING, callback=event_occurred, bouncetime=1000)
# GPIO.add_event_detect(bBTNp, GPIO.FALLING, callback=event_occurred, bouncetime=1000)

try:
    while True:
        print('Waiting button to be pressed.....')
        time.sleep(1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
