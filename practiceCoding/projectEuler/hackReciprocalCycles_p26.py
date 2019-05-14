# Enter your code here. Read input from STDIN. Print output to STDOUT

def getRecurringLength(d):
    remainder = 1 % d
    remainderList = {}
    length = 0
    n=0
    while True:
        n+=1
        if remainder * 10 > d:
            if (remainder * 10) % d == 0:
                break
            remainder = (remainder * 10) % d
            if remainder in remainderList.values():
        remainderList[n]  = remainder
                break
            remainderList[n]  = remainder

        else:
            remainderList[n]  = 0
            remainder = remainder * 10
    if len(remainderList) > 0:
        lastElement = list(remainderList.items())[-1][1]
        remainderListed = [x for x in remainderList.values()]
        if remainderListed.count(lastElement) > 1:
            length = remainderListed.index(lastElement, remainderListed.index(lastElement) + 1) - remainderListed.index(
                lastElement)

    return length


maxRecurringLengthNumberList = {}
maxLength1 = 0
d1 = 1
for i in range(2,3000):

    length1 = getRecurringLength(i)
    maxRecurringLengthNumberList[i-1] = d1
    # print(d1)
    if length1 > maxLength1:
        maxLength1 = length1
        d1 = i



# noOfTestCases = int(input().strip())
# for a0 in range(noOfTestCases):
#     N = int(input().strip())
#     maxLength = 0
#     d = 0
#     for i in range(2, N):
#
#         if i in maxRecurringLengthNumberList:
#             d = maxRecurringLengthNumberList[i]
#         else:
#             length = getRecurringLength(i)
#             if length > maxLength:
#                 maxLength = length
#                 d = i
#
#     print(d)
#
