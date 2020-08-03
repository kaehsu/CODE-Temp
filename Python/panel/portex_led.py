#!/usr/bin/env python3

import sys
import socket
import json

# Read configuration from config files
ledCONFIGfile = 'portex_led.conf'
with open(ledCONFIGfile, 'r') as file:
    ledCONFIG = file.read()

dictStatus = {
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

ledCONFIG = json.loads(ledCONFIG)
allLED = ledCONFIG.keys()
for item in allLED:
    ledCONFIG[item].update(dictStatus)
    ledCONFIG[item]['status']['opMode'].update(ledCONFIG[item]['default'])

statusFlag = {'currentStatus': 'opMode', 'lastStatus': 'opMode'}
