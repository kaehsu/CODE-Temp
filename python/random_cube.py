#!/usr/bin/env python3

import sys,time
from random import randint

N1=N2=N3=N4=N5=N6=0

start = time.clock()
for i in range(0,int(sys.argv[1])):
    N = randint(1,6)
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
stop = time.clock()

Total=N1+N2+N3+N4+N5+N6
print('Total try: {} times in {} seconds'.format(Total,stop-start))
print('N1={}({})\nN2={}({})\nN3={}({})\nN4={}({})\nN5={}({})\nN6={}({})'.format(N1, N1/Total, N2, N2/Total, N3, N3/Total, N4, N4/Total, N5, N5/Total, N6, N6/Total))
