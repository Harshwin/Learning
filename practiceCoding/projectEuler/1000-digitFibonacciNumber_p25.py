def numberOfDigits(n):
    i = 0
    while n >= 1:
        n = n // 10
        i += 1
    return i

fibcache = {}
def fib(n):

    if n == 0:
        fibcache[n] = n
        return n
    if n == 1:
        fibcache[n] = n
        return n

    if (n-1) in fibcache:
        fibcache[n] = fibcache[n-1] + fibcache[n-2]
    else:
        fibcache[n] = fib(n - 1) + fib(n - 2)
    return fibcache[n]



def fibonacci(n):
    firstNumber = 1
    SecondNumber = 2
    count = 3

    while True:
        fib = firstNumber + SecondNumber
        firstNumber = SecondNumber
        SecondNumber = fib
        count += 1

        if numberOfDigits(fib) == n:
            return count



print(fibonacci(5000))



import math
phi = 1.6180339887498948
noOfDigits = 3

d = (n * Math.log10(1.6180339887498948)) - ((Math.log10(5)) / 2);

