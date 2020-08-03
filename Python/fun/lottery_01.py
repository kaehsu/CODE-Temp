#!/usr/bin/env python3
#
#
import sys
from random import randint

existNumbers = []
newNumbers = []
seedNumbers = [5, 22, 28, 15, 19, 27]
i = 0
print(sys.argv)

while len(existNumbers) < 36:
    if i == len(seedNumbers):
        break
    seed = seedNumbers[i]
    print(i, seed)
    randomNumber = randint(1, 38)
    # print('{} is the random number this round'.format(randomNumber))
    if randomNumber in seedNumbers:
        # print('{} is seed, passed'.format(randomNumber))
        continue
    elif randomNumber in existNumbers:
        # print('{} is exist, passed'.format(randomNumber))
        continue
    elif len(newNumbers) == 6:
        print('A new number set is complete! They are ({}, {}, {}, {}, {}, {})'.format(
            seed, newNumbers[0], newNumbers[1], newNumbers[2], newNumbers[3], newNumbers[4]))
        newNumbers = []
        continue
    else:
        existNumbers.append(randomNumber)
        newNumbers.append(randomNumber)
        i += 1
existNumbers.sort()
print('The whole numbers in this round is {}, total {} numbers'.format(
    existNumbers, len(existNumbers)))
