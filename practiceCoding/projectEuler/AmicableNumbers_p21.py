def getProperDivisors(n):
    lst = [1]
    for i in range(2,int(n**0.5)+1):
        if n%i == 0 :
            lst.append(i)
            if i!=int(n**0.5):
                lst.append(int(n/i))
    return lst

def checkIfAmicable(n):
    sumOfFactors = sum(getProperDivisors(n))
    return n == sum(getProperDivisors(sumOfFactors))

if __name__== "__main__":
    #sum of all amicable numbers below 10000
    sumOfAmicableNumbers = 0

    for i in range(1,10001):
        sumOfFactors = sum(getProperDivisors(i))
        if i== sum(getProperDivisors(sumOfFactors)) and i!=sumOfFactors:
            sumOfAmicableNumbers += i
            print(i)
    print(sumOfAmicableNumbers)

def amicableNumbersList(n):
    lst = []
    for i in range(int(n)):
        sumOfFactors = sum(getProperDivisors(i))
        if i == sum(getProperDivisors(sumOfFactors)) and i != sumOfFactors:
            lst.append(i)
    return lst

