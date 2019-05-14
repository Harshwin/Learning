numberOfDigitsArray = [0] * 1001
numberOfDigitsArray[0]=''
numberOfDigitsArray[1]='one'
numberOfDigitsArray[2]='two'
numberOfDigitsArray[3]='three'
numberOfDigitsArray[4]='four'
numberOfDigitsArray[5]='five'
numberOfDigitsArray[6]='six'
numberOfDigitsArray[7]='seven'
numberOfDigitsArray[8]='eight'
numberOfDigitsArray[9]='nine'
numberOfDigitsArray[10]='ten'
numberOfDigitsArray[11]='eleven'
numberOfDigitsArray[12]='twelve'
numberOfDigitsArray[13]='thirteen'
numberOfDigitsArray[14]='fourteen'
numberOfDigitsArray[15]='fifteen'
numberOfDigitsArray[16]='sixteen'
numberOfDigitsArray[17]='seventeen'
numberOfDigitsArray[18]='eighteen'
numberOfDigitsArray[19]='nineteen'
numberOfDigitsArray[20]='twenty'
numberOfDigitsArray[30]='thirty'
numberOfDigitsArray[40]='forty'
numberOfDigitsArray[50]='fifty'
numberOfDigitsArray[60]='sixty'
numberOfDigitsArray[70]='seventy'
numberOfDigitsArray[80]='eighty'
numberOfDigitsArray[90]='ninety'
numberOfDigitsArray[100]='hundred'
numberOfDigitsArray[1000]='thousand'

def numbersToWords(n):



    if n<20:
        return numberOfDigitsArray[n]
    if n>=20 and n<100:
        return numberOfDigitsArray[int(n/10)*10] + numberOfDigitsArray[n%10]
    if n>=100 and n<1000:
        tensDigit = numberOfDigitsArray[int(str(n)[1]) * 10]
        unitsDIgit = numberOfDigitsArray[n % 10]
        if (int(str(n)[1]) * 10 + n % 10) <= 20:
            tensDigit = numberOfDigitsArray[(int(str(n)[1]) * 10 + n % 10)]
            unitsDIgit = ''
        if n%100 == 0:
            return numberOfDigitsArray[int(str(n/10)[0])] +  numberOfDigitsArray[100]
        else :
            return numberOfDigitsArray[int(str(n)[0])] +numberOfDigitsArray[100]+ 'and' + tensDigit + unitsDIgit
    else:
        return numberOfDigitsArray[1] + numberOfDigitsArray[1000]

# sumNum = 0
# for i in range(1,1001):
#     sumNum += findLenght(i)
#
# print(sumNum)

def checkAllNumbers():
    for i in range(21, 1001):
        print(numbersToWords(i))


checkAllNumbers()

def calculateLength():
    sumOfNumbers=0
    for i in range(1,1001):
        sumOfNumbers += len(numbersToWords(i))
    return sumOfNumbers

calculateLength()