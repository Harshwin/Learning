#!/bin/python3

import sys

grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
Matrix=grid
maxProduct = 0
forwardProduct = 0
downProduct = 0
forwardDiagProduct = 0
backDiagProduct = 0

for i in range(len(grid[0])):
    for j in range(len(grid[1])):
        if j <= (len(grid[1]) - 4):
            forwardProduct = Matrix[i][j] * Matrix[i][j + 1] * Matrix[i][j + 2] * Matrix[i][j + 3]
        if i <= (len(grid[0]) - 4):
            downProduct = Matrix[i][j] * Matrix[i + 1][j] * Matrix[i + 2][j] * Matrix[i + 3][j]
        if (j <= (len(grid[1]) - 4)) and (i <= (len(grid[0]) - 4)):
            forwardDiagProduct = Matrix[i][j] * Matrix[i + 1][j + 1] * Matrix[i + 2][j + 2] * Matrix[i + 3][j + 3]
        if (j >= 3 and i <= (len(grid[1]) - 4)):
            backDiagProduct = Matrix[i][j] * Matrix[i + 1][j - 1] * Matrix[i + 2][j - 2] * Matrix[i + 3][j - 3]
        maxProduct = max(maxProduct,forwardProduct,downProduct,forwardDiagProduct,backDiagProduct)

print(maxProduct)



