#!/usr/bin/env python3

import time
import datetime
import timeit


def countdown_timer(x, now=datetime.datetime.now):
    target = now()
    one_msecond_later = datetime.timedelta(milliseconds=1)
    for remaining in range(x, 0, -1):
        target += one_msecond_later
        print(datetime.timedelta(milliseconds=remaining), 'remaining', end='\r')
        if (target - now()).total_seconds() > 0:
            time.sleep((target - now()).total_seconds())
    print('\nTIMER ended')


if __name__ == '__main__':
    print(timeit.timeit(lambda: countdown_timer(6000), number=1))
