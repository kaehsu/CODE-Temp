#!/usr/bin/env python3

import os
import sys
import socket
import json
# import RPi.GPIO as GPIO

# LED configuration file and socket address
ledCONFIGfile = 'portex_led.conf'
serverAddress = '/tmp/portex_led'

# Read configuration from config files
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

'''
# GPIO initialization & enable all LED in default
GPIO.setmode(GPIO.BCM)
for item in allLED:
    GPIO.setup(ledCONFIG[item]['gpioNum'], GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)
    globals()[item+'p'] = GPIO.PWM(ledCONFIG[item]
                                   ['gpioNum'], ledCONFIG[item]['default']['freq'])
    globals()[item+'p'].start(ledCONFIG[item]['default']['dutyCycle'])
'''


def stopGPIOpwm():
    # Function to stop LED PWM and reset all LED GPIO
    for item in allLED:
        globals()[item+'p'].stop()
        GPIO.cleanup(ledCONFIG[item]['gpioNum'])
    print('All LED PWN is stop & reset')


def socketLED():
    # Unix Domain Socket for inter process communication
    try:
        # Check the socket status
        if os.path.exists(serverAddress):
            os.unlink(serverAddress)
        # Create the Unix Domain Socket
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # Bind the UDS to the port
        print('Starting up an PORTEX LED socket on {}.....'.format(
            serverAddress), file=sys.stderr)
        sock.bind(serverAddress)
        # Listen the port
        sock.listen(5)
        # Process the incoming packet
        while True:
            connection, address = sock.accept()
            serverIncoming = connection.recv(1024).decode()
            try:
                remoteCMDlist = serverIncoming.split(':')
                if remoteCMDlist[0] == 'query':
                    serverOutput = 'You execute a query command.'
                    connection.send(serverOutput.encode('utf-8'))
                    serverOutput = str(remoteCMDlist[1:])
                    connection.send(serverOutput.encode('utf-8'))
                elif remoteCMDlist[0] == 'set':
                    serverOutput = 'You execute a set command.'
                    connection.send(serverOutput.encode('utf-8'))
                    serverOutput = str(remoteCMDlist[1:])
                    connection.send(serverOutput.encode('utf-8'))
                else:
                    serverOutput = 'Not a valid command, check your syntax.'
                    connection.send(serverOutput.encode('utf-8'))
            except KeyError:
                serverOutput = 'Not a valid command, check your syntax.'
                connection.send(serverOutput.encode('utf-8'))
            connection.close()
    except KeyboardInterrupt:
        print('The server daemon stop!', file=sys.stderr)
        sock.close()


socketLED()
