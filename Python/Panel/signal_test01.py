#!/usr/bin/env python3

import signal
import time


def kbInterrupt(signum, frame):
    print()
    print('Receive keyboard interrupt')
    print()
    raise KeyboardInterrupt()


def rebuild(signum, frame):
    print('Receive Hangup')


signal.signal(signal.SIGINT, kbInterrupt)
signal.signal(signal.SIGHUP, rebuild)

while True:
    print('waiting')
    time.sleep(30)
