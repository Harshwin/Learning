

maxCount = 0
maxProduct = 0
for a in range(-1000, 1001):
    for b in range(-1000,1001):
        n = 0
        while True:
            if isPrime(n**2 + a*n + b):
                n += 1
            else:

                break
        if n > maxCount:
            print(maxCount)
            print(a,b)
            maxCount = n
            maxProduct = a*b

print(maxCount, maxProduct)




