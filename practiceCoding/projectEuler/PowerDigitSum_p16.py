import math



k = str(math.pow(2,1000))
summ=0
lst = []
while k>0:
    summ += k%10
    k = math.floor(k//10)
print(summ)

# for _ in range(int(input())):
#     print(sum(map(int, str(2 ** int(input())))))

