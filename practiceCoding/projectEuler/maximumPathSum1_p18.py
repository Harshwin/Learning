
def findMaxPath(i, j, n, triangle):
    if i == n:
        return triangle[i][j]
    else:
        return triangle[i][j] + max(findMaxPath(i+1,j-1,n, triangle),findMaxPath(i+1,j+1,n, triangle))


def formTriangle():
    numberOfRows = int(input('Enter your number of rows:').strip())
    triangleArray = [ [0] * (numberOfRows*2-1) for _ in range(numberOfRows)] # (numberOfRows)*(numberOfRows*2-1)
    columns = 0
    for a0 in range(numberOfRows):
        n = input('Enter your row by row:').strip().split(' ')
        n = [int(i) for i in n]
        j=0
        for k in range(len(n)):
            triangleArray[columns][numberOfRows - 1 - columns + j] = n[k]
            j += 2

        columns += 1

    return [triangleArray, numberOfRows]

triangleArray, numberOfRows = formTriangle()
print(findMaxPath(0,numberOfRows-1,numberOfRows-1,triangleArray))









