from math import log

k = int(input().strip())
cacheLog = []
for i in range(2,k+1):
    cacheLog.append(log(i))

lst = []

for a in range(2,k+1):
    for b in range(2,k+1):
        powers = b*cacheLog[a-2]
        powers = round(powers,2)
        if powers not in lst:
            lst.append(powers)
print(len(lst))


