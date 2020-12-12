#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

#
# Mapping the LED and relative GPIO number
gpio_gLED = 19
gpio_rLED = 26
gpio_bLED = 5
gpio_yLED = 13
gpio_oLED = 6


class portexLED:
    '''
    Build portex LED class
    '''

    def __init__(self, name, gpioPIN):
        self.name = name
        self.gpioPIN = gpioPIN

    def init(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpioPIN, GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)
        self.ledPWM = GPIO.PWM(self.gpioPIN, 1)
        self.ledPWM.start(0)
        print("{} is initialed.".format(self.name))

    def on(self):
        self.ledPWM.ChangeFrequency(1)
        self.ledPWM.ChangeDutyCycle(100)

    def on_countdown(self, timeout=5):
        led_timeout = float(timeout)
        self.ledPWM.ChangeFrequency(1)
        self.ledPWM.ChangeDutyCycle(100)
        while led_timeout > 0:
            led_timeout -= 1
            time.sleep(1)
        self.ledPWM.ChangeFrequency(1)
        self.ledPWM.ChangeDutyCycle(0)

    def off(self):
        self.ledPWM.ChangeFrequency(1)
        self.ledPWM.ChangeDutyCycle(0)

    def changePWM(self, freq, dc):
        self.ledPWM.ChangeFrequency(freq)
        self.ledPWM.ChangeDutyCycle(dc)

    def changePWM_countdown(self, n_freq, n_dc, timeout=5, o_freq=1, o_dc=0):
        led_timeout = float(timeout)
        self.ledPWM.ChangeFrequency(n_freq)
        self.ledPWM.ChangeDutyCycle(n_dc)
        while led_timeout > 0:
            led_timeout -= 1
            time.sleep(1)
        self.ledPWM.ChangeFrequency(o_freq)
        self.ledPWM.ChangeDutyCycle(o_dc)

    def reset(self):
        self.ledPWM.stop()
        GPIO.cleanup(self.gpioPIN)
        print("{} is reset.".format(self.name))


def portexLED_reset():
    for item in ledList:
        item.reset()


if __name__ == "__main__":
    try:
        gLED = portexLED('Green LED', gpio_gLED)
        rLED = portexLED('Red LED', gpio_rLED)
        bLED = portexLED('Blue LED', gpio_bLED)
        yLED = portexLED('Yellow LED', gpio_yLED)
        oLED = portexLED('Orange LED', gpio_oLED)
        ledList = [gLED, rLED, bLED, yLED, oLED]
        for item in ledList:
            item.init()
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        for item in ledList:
            item.reset()
