def findFactorial(n):
    if n==1:
        return 1
    else:
        return n*findFactorial(n-1)

factorial = findFactorial(100)
sumOfDigits = sum([int(i) for i in str(factorial)])
