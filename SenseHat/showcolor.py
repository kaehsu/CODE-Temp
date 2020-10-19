#!/usr/bin/env python3

from sense_hat import SenseHat
from random import randint

sense = SenseHat()

r = randint(0,randint(1,255))
g = randint(0,randint(1,255))
b = randint(0,randint(1,255))

print("R, G, B values are", r, g ,b)

sense.clear((r, g, b))

