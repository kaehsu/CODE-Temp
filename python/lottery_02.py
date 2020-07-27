#!/usr/bin/env python3
#
#
import sys
from random import randint

existNumbers = []
newNumbers = []

while len(existNumbers) < 36:
    randomNumber = randint(1, 38)
    # print('{} is the random number this round'.format(randomNumber))
    if randomNumber in existNumbers:
        # print('{} is exist, passed'.format(randomNumber))
        continue
    elif len(newNumbers) == 6:
        print('A new number set is complete! They are ({}, {}, {}, {}, {}, {})'.format(
            newNumbers[0], newNumbers[1], newNumbers[2], newNumbers[3], newNumbers[4], newNumbers[5]))
        newNumbers = []
        continue
    else:
        existNumbers.append(randomNumber)
        newNumbers.append(randomNumber)
existNumbers.sort()
print('The whole numbers in this round is {}, total {} numbers'.format(
    existNumbers, len(existNumbers)))
