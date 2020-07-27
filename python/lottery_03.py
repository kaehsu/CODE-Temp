#!/usr/bin/env python3
#
#
from random import randint, seed
from itertools import combinations

seedNumbers1 = [5, 22, 28, 15, 19, 24, 12, 23]
seedNumbers2 = [27, 8, 10]
newNumbers = []

# Step one, list all possible combinations of seedNumbers1
comb_list1 = []
for combNumber in combinations(seedNumbers1, 6):
    comb_list1.append(combNumber)
print(comb_list1)
print('There are total {} combinations from seedNumbers1, it will cost {} dollors.\n'.format(
    len(comb_list1), len(comb_list1)*8*100))

# Step two, list all combination based on seedNumbers1
comb_list2 = []
for i in range(0, len(seedNumbers1)):
    # print(seedNumbers[i])
    newNumbers.append(seedNumbers1[i])
    seed(seedNumbers1[i])
    for j in range(0, 5):
        rN = randint(1, 38)
        if rN in newNumbers:
            NrN = randint(1, 38)
            print('Duplicate number {} found! Will replace to {}'.format(rN, NrN))
            newNumbers.append(NrN)
        else:
            newNumbers.append(rN)
        if len(newNumbers) == 6:
            # print(newNumbers)
            comb_list2.append(newNumbers)
            newNumbers = []
print(comb_list2)
print('There are total {} combinations from random number(seed by seedNumbers1), it will cost {} dollors.\n'.format(
    len(comb_list2), len(comb_list2)*8*100))

# Step three, list all combination based on seedNumbers2
comb_list3 = []
newNumbers = []
for i in range(0, len(seedNumbers2)):
    # print(seedNumbers2[i])
    newNumbers.append(seedNumbers2[i])
    seed(seedNumbers2[i])
    for j in range(0, 5):
        rN = randint(1, 38)
        if rN in newNumbers:
            NrN = randint(1, 38)
            print('Duplicate number {} found! Will replace to {}'.format(rN, NrN))
            newNumbers.append(NrN)
        else:
            newNumbers.append(rN)
        if len(newNumbers) == 6:
            # print(newNumbers)
            comb_list3.append(newNumbers)
            newNumbers = []
print(comb_list3)
print('There are total {} combinations from random number(seed by seedNumbers2), it will cost {} dollors.\n'.format(
    len(comb_list3), len(comb_list3)*8*100))

print('Total cost is {}'.format(len(comb_list1)*8*100 +
                                len(comb_list2)*8*100 + len(comb_list3)*8*100))
