# def generateSpiralMatrix(n):
#     initialPoint = int(n/2)
#     matrix = [[0 for x in range(n)] for y in range(n)]
#     i = 1
#     num = 25
#     count = 0
#     matrix[initialPoint][initialPoint] = 1
#     for x,y in zip(range(0,n),range(n-1,-1,-1)):
#         for i in range(n-1+x,-1+x,-1):
#             matrix[count][i] = num
#             num -= 1
#
#
#         for j in range(0+x,n-x):
#             matrix[j][count] = num
#             num -= 1
#
#         for k in range(0+x, n-x):
#             matrix[4-count][k] = num
#             num -= 1
#
#
#         for l in range(n-1-x,0+x,-1):
#             matrix[l][y] = num
#             num -= 1
#
#         count += 1
#         if x == initialPoint and y == initialPoint:
#             break
#
#     return matrix
#
# print(generateSpiralMatrix(5))
#
#
#
k=1001
sumOfDiagonals = 1
for n in range(1,int(k/2)+1):
    sumOfDiagonals += 4*(4*n**2 + n + 1)
print(sumOfDiagonals)