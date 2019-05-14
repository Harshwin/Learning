import time
startTime = time.time()

def getProperDivisors(n):
    lst = [1]
    for i in range(2,int(n**0.5)+1):
        if n%i == 0 :
            lst.append(i)
            if i!=n**0.5:
                lst.append(int(n/i))
    return lst

def checkIfAbundant(n):
    return n < sum(getProperDivisors(n))

lst = [False for x in range(28124)]
for i in range(1,28124):
    if checkIfAbundant(i):
        lst[i]= True


sumOfAbundantNumbers = 0
for i in range(1,28124):
    for j in range(1,i):
        if lst[j] and lst[i-j]:
            #print(i, j, i-j)
            sumOfAbundantNumbers += i
            break

print(sum(list(range(1,28124)))- sumOfAbundantNumbers)

print('time taken = ', time.time() - startTime)