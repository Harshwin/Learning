def isPrime(n):
    n=abs(n)
    if n==1 or n==0:
        return False
    if n==2:
        return True
    if (n%2 == 0):
        return False
    for x in range(3,int(n**0.5+1),2):
            if n%x==0:
                return False
    else:
        return True


def getLcm(a, b):
    lcm = 1
    #    minOfGivenNumbers=np.min(a,b)
    i = 1
    #    for i in range(1,min(a,b)+1):
    while i < (min(a, b) + 1):

        if (isPrime(i) and b % i == 0 and a % i == 0):
            b = b / i
            a = a / i
            #            print('a ',a)
            #            print('b ',b)
            #            print('i ',i)
            lcm = lcm * i
            i = 1
        #            print('lcm ', lcm)
        i = incrementByOne(i)

    return lcm * a * b


def incrementByOne(i):
    i = i + 1
    return i


print(getLcm(8,12))
