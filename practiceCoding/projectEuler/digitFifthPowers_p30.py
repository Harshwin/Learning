def sumOfPowers(n,k):
    summ =0
    remainder = 0
    for i in range(len(str(n))):
        remainder = n%10
        summ = summ + remainder**k
        n=int(n/10)
    return summ


sumo = 0
for i in range(10,100000000):
    if sumOfPowers(i,5) == i:
        sumo = sumo + i
        print(i)

print(sumo)