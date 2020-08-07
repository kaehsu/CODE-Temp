#!/usr/bin/env python3

import os
import sys
from pprint import pprint
import json

ledCONFIGfile = 'portex_led.conf'

# Read configuration file
global ledCONFIG
with open(ledCONFIGfile, 'r') as file:
    ledCONFIG = file.read()
# Data structure that did not be included in configuration file
ledModetemp = {
    "ledList": "gLED,rLED,bLED,yLED,oLED",
    "currentMode": "opMode",
    "lastMode": "opMode"
}
ledStatustemp = {
    "opMode": {
        "freq": 1,
        "dutyCycle": 0
    },
    "adMode": {
        "freq": 1,
        "dutyCycle": 0
    }

}
# Build LED configuration data structure
ledCONFIG = json.loads(ledCONFIG)
ledCONFIG['allLED'].update(ledModetemp)
ledCONFIG['allLED']['powerSave']['timer'] = ledCONFIG['allLED']['powerSave']['timeout']
global allLEDlist
allLEDlist = ledCONFIG['allLED']['ledList'].split(',')
for item in allLEDlist:
    ledCONFIG[item].update(ledStatustemp)
    # Didn't work, use the following statement instead
    # ledCONFIG[item]['opMode'].update(ledCONFIG[item]['default'])
ledCONFIG['gLED']['opMode'].update(ledCONFIG['gLED']['default'])
ledCONFIG['rLED']['opMode'].update(ledCONFIG['rLED']['default'])
ledCONFIG['bLED']['opMode'].update(ledCONFIG['bLED']['default'])
ledCONFIG['yLED']['opMode'].update(ledCONFIG['yLED']['default'])
ledCONFIG['oLED']['opMode'].update(ledCONFIG['oLED']['default'])
