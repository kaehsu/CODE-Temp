#!/usr/bin/env python3

import time

t = 10

while t > 0:
    print("{:02d} seconds remained.".format(t))
    t -= 1
    time.sleep(1)

print("Timeout.")
