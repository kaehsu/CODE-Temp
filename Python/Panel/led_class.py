#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time


class LED:
    '''
    Build LED class
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

    def off(self):
        self.ledPWM.ChangeFrequency(1)
        self.ledPWM.ChangeDutyCycle(0)

    def changePWM(self, freq, dc):
        self.ledPWM.ChangeFrequency(freq)
        self.ledPWM.ChangeDutyCycle(dc)

    def reset(self):
        self.ledPWM.stop()
        GPIO.cleanup(self.gpioPIN)
        print("{} is reset.".format(self.name))


if __name__ == "__main__":
    gLED = LED('gLED', 19)
    print(gLED.name)
    gLED.init()
    gLED.on()
    time.sleep(3)
    gLED.changePWM(2, 50)
    time.sleep(3)
    gLED.off()
    gLED.reset()
