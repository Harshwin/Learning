def charTONumber(n):
    num = ord(n)

    if len(n)!=1:
        return 0

    else:
        return (num - 64 ) # as only capital letters are there


numberOfNames = int(input().strip())
namesList = []
for a0 in range(numberOfNames):
    name = str(input().strip()).upper()
    namesList.append(name)

namesList.sort()
noOfTestNames = int(input().strip())
for b0 in range(noOfTestNames):
    testName = str(input().strip()).upper()
    print(sum(list(map(lambda X : charTONumber(X),testName))) * (namesList.index(testName)+1) )

