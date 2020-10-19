#!/usr/bin/env python3

from sense_hat import SenseHat
from random import randint
from time import sleep
import subprocess

sense = SenseHat()

subprocess.Popen(['/home/pi/SenseHat/white_on.sh'])
sleep(1)

sense.set_rotation(90)
letters=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
count=0
loop=randint(1,26)
pause=1

try:
    print("Random show letter", loop ,"times.")
    while count<loop:
        sense.show_letter(letters[randint(0,25)])
        count+=1
        print(count)
        sleep(pause)
        sense.clear()

    print("Action is complete")
    sleep(1)
    sense.clear()
    subprocess.Popen(['/home/pi/SenseHat/white_off.sh'])
    
except KeyboardInterrupt:
    print("")
    sense.clear()
    subprocess.Popen(['/home/pi/SenseHat/white_off.sh'])
