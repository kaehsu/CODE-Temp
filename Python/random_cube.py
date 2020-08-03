#!/usr/bin/env python3

import sys
import time
import threading
from random import randint

T = int(sys.argv[1]) // 6
T6 = int(sys.argv[1])-T*5


def cube_try(n):
    global N1, N2, N3, N4, N5, N6
    for i in range(0, n):
        N = randint(1, 6)
        if N == 1:
            N1 += 1
        elif N == 2:
            N2 += 1
        elif N == 3:
            N3 += 1
        elif N == 4:
            N4 += 1
        elif N == 5:
            N5 += 1
        elif N == 6:
            N6 += 1


def main():
    global T6, T, N1, N2, N3, N4, N5, N6
    threading.Thread(target=cube_try(T6)).start()
    threading.Thread(target=cube_try(T)).start()
    threading.Thread(target=cube_try(T)).start()
    threading.Thread(target=cube_try(T)).start()
    threading.Thread(target=cube_try(T)).start()
    threading.Thread(target=cube_try(T)).start()


start = time.process_time()
N1 = N2 = N3 = N4 = N5 = N6 = 0
main()
stop = time.process_time()

Total = N1+N2+N3+N4+N5+N6
print('Total try: {} times in {} seconds'.format(Total, stop-start))
print('N1={}({:.5f})\nN2={}({:.5f})\nN3={}({:.5f})\nN4={}({:.5f})\nN5={}({:.5f})\nN6={}({:.5f})'.format(
    N1, N1/Total, N2, N2/Total, N3, N3/Total, N4, N4/Total, N5, N5/Total, N6, N6/Total))
