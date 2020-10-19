#!/usr/bin/env python3

from sense_hat import SenseHat
from random import randint

sense = SenseHat()

r = 0
g = 0
b = 0

print("R, G, B values are", r, g ,b)

sense.clear((r, g, b))
