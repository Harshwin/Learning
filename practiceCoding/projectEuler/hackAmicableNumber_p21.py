# Enter your code here. Read input from STDIN. Print output to STDOUT
def getProperDivisors(n):
    lst = [1]
    for i in range(2,int(n**0.5)+1):
        if n%i == 0 :
            lst.append(i)
            if i!=int(n**0.5):
                lst.append(int(n/i))
    return lst


def amicableNumbersList(n):
    lst = []
    for i in range(int(n)):
        sumOfFactors = sum(getProperDivisors(i))
        if i == sum(getProperDivisors(sumOfFactors)) and i != sumOfFactors:
            lst.append(i)
    return lst

list5 = amicableNumbersList(100000)

testCases = int(input().strip())
for a0 in range(testCases):
    number = int(input().strip())
    print(sum([x for x in list5 if x < number]))



