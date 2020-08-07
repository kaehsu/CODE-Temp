#!/usr/bin/env python3

import os
import sys
from pprint import pprint
import socket
import json
# import RPi.GPIO as GPIO
import threading
import copy

# LED configuration file and socket address
ledCONFIGfile = 'portex_led.conf'
serverAddress = '/tmp/portex_led'


def configInit(configFile=ledCONFIGfile):
    '''
    Initial the LED configuration data structure
    '''
    # Read configuration file
    global ledCONFIG
    with open(configFile, 'r') as file:
        ledCONFIG = file.read()
    # Data structure that did not be included in configuration file
    ledModetemp = {
        "ledList": "gLED,rLED,bLED,yLED,oLED",
        "currentMode": "opMode",
        "lastMode": "opMode"
    }
    ledStatustemp = {
        "opMode": {
            "freq": 0,
            "dutyCycle": 0
        },
        "adMode": {
            "freq": 0,
            "dutyCycle": 0
        }
    }
    # Build LED configuration data structure
    ledCONFIG = json.loads(ledCONFIG)
    ledCONFIG['allLED'].update(ledModetemp)
    ledCONFIG['allLED']['powerSave']['timer'] = ledCONFIG['allLED']['powerSave']['timeout']
    global allLEDlist
    allLEDlist = tuple(ledCONFIG['allLED']['ledList'].split(','))
    for item in allLEDlist:
        # deepcopy could deuplicate ledStatustemp with different id, but need import copy first.
        # All other attempts to try to duplicate ledStatustemp are failed.
        ledCONFIG[item].update(copy.deepcopy(ledStatustemp))
        print(id(ledCONFIG[item]['opMode']), id(ledCONFIG[item]['adMode']))
        # Didn't work, use the following statement instead
        ledCONFIG[item]['opMode'].update(ledCONFIG[item]['default'])


def printConfig():
    return(ledCONFIG)


def configQuery(dictKeylist):
    '''
    Print the value by query key list, the first element in the list must 'query'.
    The answer could be a str(), int() or dict().
    '''
    if dictKeylist[0] != 'query':
        return 'Not a valid qurey, check your syntax.'
    try:
        cqResult = ledCONFIG
        for item in range(1, len(dictKeylist)):
            cqResult = cqResult[dictKeylist[item]]
        return cqResult
    except (NameError, TypeError, KeyError) as e:
        return 'Not a valid query, check your syntax.'


def configChange(dictKeylist):
    '''
    Change the LED configuration.
    '''
    if dictKeylist[0] != 'set':
        return 'Not a valid change, check your syntax.'
    try:
        ccTargetold = ledCONFIG
        for item in range(1, len(dictKeylist)-1):
            ccTargetold = ccTargetold[dictKeylist[item]]
        ccTargetpath = 'ledCONFIG'
        for item in range(1, len(dictKeylist)-1):
            ccTargetpath = ccTargetpath+"['"+str(dictKeylist[item])+"']"
        if type(ccTargetold) == type(int()):
            ccTargetnew = int(dictKeylist[-1])
            changeCMD = ccTargetpath+'='+str(ccTargetnew)
            exec(changeCMD)
            return 'Value ' + str(ccTargetold) + ' change to ' + str(ccTargetnew)
        elif type(ccTargetold) == type(str()):
            ccTargetnew = str(dictKeylist[-1])
            changeCMD = ccTargetpath+"='"+str(ccTargetnew)+"'"
            exec(changeCMD)
            return 'Value ' + str(ccTargetold) + ' change to ' + str(ccTargetnew)
    except (NameError, TypeError, KeyError, ValueError) as e:
        return 'Not a valid change exp, check your syntax.'


def initGPIOpwm():
    '''
    GPIO initialization & enable all LED by default configuration.
    '''
    GPIO.setmode(GPIO.BCM)
    for item in allLEDlist:
        GPIO.setup(ledCONFIG[item]['gpioNum'],
                   GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)
        globals()[item+'p'] = GPIO.PWM(ledCONFIG[item]
                                       ['gpioNum'], ledCONFIG[item]['default']['freq'])
        globals()[item+'p'].start(ledCONFIG[item]['default']['dutyCycle'])
    return 'All LED pWM is enable and stay in default status.'


def stopGPIOpwm():
    '''
    Function to stop LED PWM and reset all LED GPIO
    '''
    for item in allLEDlist:
        globals()[item+'p'].stop()
        GPIO.cleanup(ledCONFIG[item]['gpioNum'])
    return 'All LED PWN is stop & reset.'


def ledSocket():
    '''
    Unix Domain Socket for inter process communication
    '''
    try:
        # Check the socket status; if occupied, reset it.
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
                global remoteCMDlist
                remoteCMDlist = serverIncoming.split(':')
                print('Received incoming message: {}.....'.format(
                    remoteCMDlist), file=sys.stderr)
                if remoteCMDlist[0] == 'query':
                    queryResult = configQuery(remoteCMDlist)
                    serverOutput = str(queryResult)
                    connection.send(serverOutput.encode('utf-8'))
                elif remoteCMDlist[0] == 'set':
                    setResult = configChange(remoteCMDlist)
                    serverOutput = 'set result: ' + str(setResult)
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


def main():
    configInit()
    # initGPIOpwm()
    threadSocket = threading.Thread(target=ledSocket)
    threadSocket.setDaemon(True)
    threadSocket.start()
    # stopGPIOpwm()


if __name__ == '__main__':
    main()
