#!/usr/bin/env python3

from sense_hat import SenseHat
from random import randint
from time import sleep
import subprocess

sense = SenseHat()

subprocess.Popen(['/home/pi/SenseHat/yellow_on.sh'])
sleep(1)
sense.set_rotation(90)
loop=64
s=0.1

try:
    while True:
        count=0
        rate=randint(1,8)
        while count<loop:
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            h = randint(0,7)
            v = randint(0,7)
            sense.set_pixel(h, v, (r, g, b))
            count+=1
            print(count)
            sleep(s)

        print("Add action is complete, will continous after 3 seconds...")
        sleep(3)
        count=0

        while count<(loop*rate):
            h = randint(0,7)
            v = randint(0,7)
            sense.set_pixel(h, v, (0, 0, 0))
            count+=1
            print(count)
            sleep(s/rate)

        print("Delete action is complete, will end after 5 seconds.....")
        sleep(5)
        sense.clear()
    
except KeyboardInterrupt:
    print("")
    sense.clear()
    subprocess.Popen(['/home/pi/SenseHat/yellow_off.sh'])
