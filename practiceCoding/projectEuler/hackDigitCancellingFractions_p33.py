import math
from itertools import combinations

# TODO:  write gcd function

# program to convert a list
# of integers into a single integer
def convert(list):
    # Converting integer list to string list
    if list == []:
        return 0
    s = [str(i) for i in list]

    # Join list items using join()
    res = int("".join(s))

    return (res)



n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
upperLimit = 1

for i in range(n):
    upperLimit*= 10


sumOfNumerator = 0
sumOfDenominator = 0


for num in range(int(upperLimit/10),upperLimit):
    for den in range(num+1,upperLimit):
        numeratorList = [int(i) for i in str(num)]
        denominatorList = [int(i) for i in str(den)]

        commonTerms = [x for x in numeratorList if x in denominatorList]
        variousCombinationsOfCommonTerms = list(combinations(commonTerms, k))
        for i in range(k + 1):
            numeratorRemainingTerms = convert([x for x in numeratorList if x not in variousCombinationsOfCommonTerms[i]])

            denominatorRemainingTerms = convert([x for x in denominatorList if x not in variousCombinationsOfCommonTerms[i]])
            if numeratorRemainingTerms / denominatorRemainingTerms == num/den:
                sumOfNumerator += num
                sumOfDenominator += den



print(sumOfNumerator, sumOfDenominator)