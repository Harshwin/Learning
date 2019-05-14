def numberOfDivisors(n):
    count = 0
    powersOfPrime = {}
    i=2
    while i <= int(n):
        if n%i == 0:
            count+=1
            n = n/i
            if i in powersOfPrime:
                powersOfPrime[i] = powersOfPrime[i] + 1
                # print("powers", powersOfPrime)

            else:
                powersOfPrime[i] = 2
        else:
            i=i+1

    totalDivisors = 1
    for value in powersOfPrime.values():
        totalDivisors = totalDivisors * value
    return totalDivisors

print(numberOfDivisors(4200))