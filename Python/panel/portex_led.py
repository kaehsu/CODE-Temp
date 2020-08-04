#!/usr/bin/env python3

import sys
import socket
import json
import RPi.GPIO as GPIO

# Read configuration from config files
ledCONFIGfile = 'portex_led.conf'
with open(ledCONFIGfile, 'r') as file:
    ledCONFIG = file.read()

ledStatustemp = {
    "status": {
        "opMode": {
            "freq": 0,
            "dutyCycle": 0
        },
        "adMode": {
            "freq": 0,
            "dutyCycle": 0
        }
    }
}

# Build necessary data structure
ledCONFIG = json.loads(ledCONFIG)
allLED = ledCONFIG['allLED']['allLED'].split(',')
for item in allLED:
    ledCONFIG[item].update(ledStatustemp)
    ledCONFIG[item]['status']['opMode'].update(ledCONFIG[item]['default'])

# GPIO initialization
GPIO.setmode(GPIO.BCM)
for item in allLED:
    GPIO.setup(ledCONFIG[item]['gpioNum'], GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)
    str(item)+'p' = GPIO.PWM(ledCONFIG[item]['gpioNum'], 1)
