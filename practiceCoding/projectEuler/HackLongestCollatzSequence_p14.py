#!/bin/python3

import sys

preCalcTill = 5000000

def findChain(n):
    # if n<preCalcTill and dictionary[int(n)!=0 ]:
    #     return longestTillTime[int(n)]
    if (n == 1):
        return 1
    elif (n in dictionary):
        return dictionary[n]
    elif (n % 2 == 0):

        tempCount = 1 + findChain(n / 2)
        dictionary[n] = int(tempCount)
        return tempCount
    else:
        tempCount = 1 + findChain(3 * n + 1)
        dictionary[n] = tempCount
        return (tempCount)

currentChainLength = 0
longestTillTime = {}
for j in range(1,preCalcTill):
    currentChainLength = findChain(j)
    if maxCount <= count:
        maxCount = count
        maxCountAt = i
    longestTillTime[j] = maxCountAt




t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    count = 0
    maxCount = 0
    maxCountAt = 0
    dictionary = {}
    if n < preCalcTill :
        print(longestTillTime[n])
    else:

        for i in range(1, n + 1):
            count = findChain(i)  ### Redunted parameter check with keerthi for a tip
            dictionary[i] = count

            if maxCount <= count:
                maxCount = count
                maxCountAt = i
        print(maxCountAt)



