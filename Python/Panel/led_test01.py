#!/usr/bin/env python3

from led_class import portexLED
import time

gpio_yLED = 13
gpio_oLED = 6
gpio_gLED = 19
gpio_bLED = 5
gpio_rLED = 26

gLED = portexLED('Green LED', gpio_gLED)
rLED = portexLED('Red LED', gpio_rLED)
bLED = portexLED('Blue LED', gpio_bLED)
yLED = portexLED('Yellow LED', gpio_yLED)
oLED = portexLED('Orange LED', gpio_oLED)

ledList = [gLED, rLED, bLED, yLED, oLED]


def allLED_init():
    for item in ledList:
        item.init()


def allLED_reset():
    for item in ledList:
        item.reset()


try:
    allLED_init()

    for item in ledList:
        item.on()
        time.sleep(1)

    time.sleep(3)

    for item in ledList:
        item.off()
        time.sleep(1)
except KeyboardInterrupt:
    allLED_reset()

print('LED program is complete.')
allLED_reset()
