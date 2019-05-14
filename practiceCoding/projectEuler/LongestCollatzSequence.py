import time


def findChain(n):
    if (n==1):
        return 1
    elif (n in dictionary):
        return dictionary[n]
    elif (n%2==0):
        tempCount = 1 + findChain(n/2)
        dictionary[n] = tempCount
        return tempCount
    else:
        tempCount = 1 + findChain(3 * n + 1)
        dictionary[n]=tempCount
        return tempCount


count = 0
maxCount=0
maxCountAt = 0
dictionary = {}
k= 5
for i in range(2,k+1):
    count = findChain(i)


    if maxCount <= count :

        maxCount = count
        maxCountAt = i
        longestTillTime[i] = maxCountAt

print(maxCountAt)
