numberOfDigitsArray = [0] * 1001
numberOfDigitsArray[0]=''
numberOfDigitsArray[1]='One'
numberOfDigitsArray[2]='Two'
numberOfDigitsArray[3]='Three'
numberOfDigitsArray[4]='Four'
numberOfDigitsArray[5]='Five'
numberOfDigitsArray[6]='Six'
numberOfDigitsArray[7]='Seven'
numberOfDigitsArray[8]='Eight'
numberOfDigitsArray[9]='Nine'
numberOfDigitsArray[10]='Ten'
numberOfDigitsArray[11]='Eleven'
numberOfDigitsArray[12]='Twelve'
numberOfDigitsArray[13]='Thirteen'
numberOfDigitsArray[14]='Fourteen'
numberOfDigitsArray[15]='Fifteen'
numberOfDigitsArray[16]='Sixteen'
numberOfDigitsArray[17]='Seventeen'
numberOfDigitsArray[18]='Eighteen'
numberOfDigitsArray[19]='Nineteen'
numberOfDigitsArray[20]='Twenty'
numberOfDigitsArray[30]='Thirty'
numberOfDigitsArray[40]='Forty'
numberOfDigitsArray[50]='Fifty'
numberOfDigitsArray[60]='Sixty'
numberOfDigitsArray[70]='Seventy'
numberOfDigitsArray[80]='Eighty'
numberOfDigitsArray[90]='Ninety'
numberOfDigitsArray[100]='Hundred'
numberOfDigitsArray[1000]='Thousand'





def betweenMillionAndBillion(n):



    if (n/1000000).is_integer() :
        return numbersToWords(int(str(n)[:-6])) + ' ' + 'Million'

    if int(str(n)[:-6]) < 100:
        tenMillionsDigit = numberOfDigitsArray[int(str(n)[0]) * 10]
        millionsDigit = numberOfDigitsArray[int(str(n)[1])] + ' '
        if (int(str(n)[0]) * 10 + int(str(n)[1])) <= 20:
            tenMillionsDigit = numberOfDigitsArray[(int(str(n)[0]) * 10 + int(str(n)[1]))]
            millionsDigit = ''

        return tenMillionsDigit +' ' + millionsDigit + 'Million' + ' ' + numbersToWords(int(str(n)[-6:]))
    if int(str(n)[:-6]) > 100:
        tenMillionsDigit = numberOfDigitsArray[int(str(n)[1]) * 10]
        millionsDigit = numberOfDigitsArray[int(str(n)[2])] + ' '
        if (int(str(n)[1]) * 10 + int(str(n)[2])) <= 20:
            tenMillionsDigit = numberOfDigitsArray[(int(str(n)[1]) * 10 + int(str(n)[2]))]
            millionsDigit = ''

        return numberOfDigitsArray[int(str(n)[0])] +' ' + 'Hundred ' + tenMillionsDigit +' ' + millionsDigit + 'Million' + ' ' + numbersToWords(int(str(n)[-6:]))



def between1000andMillion(n):

    x = 0

    if (n/1000).is_integer() :
        return numbersToWords(int(str(n)[:-3])) + ' ' + numberOfDigitsArray[1000]

    if n<100000:
        tenThousandDigit = numberOfDigitsArray[int(str(n)[0]) * 10]
        thousandsDigit = numberOfDigitsArray[int(str(n)[1])] + ' '
        if (int(str(n)[0]) * 10 + int(str(n)[1])) <= 20:
            tenThousandDigit = numberOfDigitsArray[(int(str(n)[0]) * 10 + int(str(n)[1]))]
            thousandsDigit = ''

        return tenThousandDigit +' ' + thousandsDigit + numberOfDigitsArray[1000] + ' ' + numbersToWords(int(str(n)[-3:]))
    if n>100000:
        tenThousandDigit = numberOfDigitsArray[int(str(n)[1]) * 10]
        thousandsDigit = numberOfDigitsArray[int(str(n)[2])] + ' '
        if (int(str(n)[1]) * 10 + int(str(n)[2])) <= 20:
            tenThousandDigit = numberOfDigitsArray[(int(str(n)[1]) * 10 + int(str(n)[2]))]
            thousandsDigit = ''

        return numberOfDigitsArray[int(str(n)[0])] +' ' + 'Hundred ' + tenThousandDigit +' ' + thousandsDigit + numberOfDigitsArray[1000] + ' ' + numbersToWords(int(str(n)[-3:]))


def between100and1000(n):
    tensDigit = numberOfDigitsArray[int(str(n)[1]) * 10]
    unitsDIgit = numberOfDigitsArray[n % 10]
    if (int(str(n)[1]) * 10 + n % 10) <= 20:
        tensDigit = numberOfDigitsArray[(int(str(n)[1]) * 10 + n % 10)]
        unitsDIgit = ''

    if n % 100 == 0:
        return numberOfDigitsArray[int(str(n / 10)[0])] + ' ' + numberOfDigitsArray[100]

    else:
        return numberOfDigitsArray[int(str(n)[0])] +' '+ numberOfDigitsArray[100] + ' ' + tensDigit + ' ' + unitsDIgit


def between20and100(n):
    return numberOfDigitsArray[int(n / 10) * 10] + ' ' + numberOfDigitsArray[n % 10]


def lessThan20(n):
    return numberOfDigitsArray[n]

def betweenBillionAndTrillion(n):
    if (n/1000000000).is_integer() :
        return numbersToWords(int(str(n)[:-9])) + ' ' + 'Billion'

    if int(str(n)[:-9]) < 100:
        tenBillionsDigit = numberOfDigitsArray[int(str(n)[0]) * 10]
        billionsDigit = numberOfDigitsArray[int(str(n)[1])] + ' '
        if (int(str(n)[0]) * 10 + int(str(n)[1])) <= 20:
            tenBillionsDigit = numberOfDigitsArray[(int(str(n)[0]) * 10 + int(str(n)[1]))]
            billionsDigit = ''

        return tenBillionsDigit +' ' + billionsDigit + 'Billion ' + numbersToWords(int(str(n)[-9:]))
    if int(str(n)[:-9]) > 100:
        tenBillionsDigit = numberOfDigitsArray[int(str(n)[1]) * 10]
        BillionsDigit = numberOfDigitsArray[int(str(n)[2])] + ' '
        if (int(str(n)[1]) * 10 + int(str(n)[2])) <= 20:
            tenBillionsDigit = numberOfDigitsArray[(int(str(n)[1]) * 10 + int(str(n)[2]))]
            billionsDigit = ''

        return numberOfDigitsArray[int(str(n)[0])] + ' ' + 'Hundred ' + tenBillionsDigit +' ' + billionsDigit + 'Billion ' + numbersToWords(int(str(n)[-9:]))




def numbersToWords(n):



    if n<20:
        return lessThan20(n)
    if n>=20 and n<100:
        return between20and100(n)
    if n>=100 and n<1000:
        return between100and1000(n)
    if n >= 1000 and n<1000000:
        return between1000andMillion(n)
    if n >= 1000000 and n<1000000000:
        return betweenMillionAndBillion(n)
    if n>=1000000000 and n<1000000000000:
        return betweenBillionAndTrillion(n)

betweenBillionAndTrillion(12345678090)


# sumNum = 0
# for i in range(1,1001):
#     sumNum += findLenght(i)
#
# print(sumNum)
# import math
#
# def checkAllNumbers():
#     for i in range(1,int(math.pow(10,12))+1 ):
#         print(numbersToWords(i))
#
#
# checkAllNumbers()

