
def getRecurringLength(d):
    remainder = 1%d
    remainderList = []
    length = 0
    while True:

        if remainder * 10 > d:
            if (remainder * 10) % d == 0:
                break
            remainder = (remainder * 10) % d
            if remainder in remainderList:
                remainderList.append(remainder)
                break
            remainderList.append(remainder)

        else:
            remainderList.append(0)
            remainder = remainder * 10
    if len(remainderList)>0:
        lastElement = remainderList[-1]
        if remainderList.count(lastElement) > 1:
            length = remainderList.index(lastElement, remainderList.index(lastElement) + 1) - remainderList.index(lastElement)

    return length


maxLength = 0
d = 0
for i in range(2,1000):
    print('i',i)

    length = getRecurringLength(i)
    if length > maxLength:
        maxLength = length
        d=i
        print(d)


print(d, maxLength)






























# def recurringCycleLength(decimalPart):
#     window = 1
#     length = 0
#     while len(decimalPart)> window:
#         subNumber = decimalPart[:window]
#
#
#         for j in subNumber:
#             if subNumber.count(j)>1:
#                 length =  subNumber.find(j,subNumber.find(j)+1) - subNumber.find(j)
#
#
#         window +=1
#
#
#     return length
#
#
# maxLength = 0
# d = 0
# for i in range(1,1000):
#     fraction = 1/i
#     decimalPart = str(fraction).split('.')[1]
#     length = recurringCycleLength(decimalPart)
#     if length > maxLength:
#         maxLength = length
#         d = i
#
# print(d, maxLength)

