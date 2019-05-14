
#what happens to 0? can it repeat?
def checkPandigital(n,k):
    numberList=[int(i) for i in str(n)]
    pandigital = list(range(1,k+1))
    if len(str(n)) != k:
        return False
    if numberList.count(0)>0 or [True for x in pandigital if x not in numberList]:
        return False
    if [True for x in pandigital if numberList.count(x)>1]:
        return False
    else:
        return True
def getUpperLimit(n):
    upperLimit = 1
    n=int(n/2)
    for i in range(n):
        upperLimit *= 10
    return upperLimit

sumOfPandigitalNumbers = 0
setOfProduct = set()
k=4
upperLimit =getUpperLimit(k)
for i in range(1,upperLimit):
    for j in range(1,int(upperLimit/i)):
        product = i*j
        number = int(str(i)+str(j)+str(product))
        if (checkPandigital(number,k)):
            print(number)
            setOfProduct.add(product)


print(sum(setOfProduct))