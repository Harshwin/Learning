# Enter your code here. Read input from STDIN. Print output to STDOU
from math import log10, ceil


def getNumberOfDigitsOfFib(n):
    d = (n * log10(1.6180339887498948) - ((log10(5)) / 2))
    return ceil(d)


numberOfDigitsList = []
for i in range(1,5000):
    numberOfDigitsList.append(getNumberOfDigitsOfFib(i))

noOfTestCases = int(input().strip())
for a0 in range(noOfTestCases):
    noOfDigits = int(input().strip())
    print(numberOfDigitsList.index(noOfDigits)+1)

