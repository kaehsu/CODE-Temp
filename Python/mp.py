#!/usr/bin/env python3

import multiprocessing
import os


def whoami(what):
    print("Process {} says: {}".format(os.getpid(), what))


if __name__ == '__main__':
    whoami("I'm the main program")
    for n in range(64):
        p = multiprocessing.Process(
            target=whoami, args=("I'm function %s" % n,))
        p.start()
quit9
