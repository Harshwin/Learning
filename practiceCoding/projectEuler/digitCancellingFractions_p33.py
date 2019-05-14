import math

# TODO:  write gcd function
def getProperDivisors(n):
    lst = [1]
    for i in range(2,int(n**0.5)+1):
        if n%i == 0 :
            lst.append(i)
            if i!=n**0.5:
                lst.append(int(n/i))
    return lst

numeratorProduct = 1
denominatorProduct = 1
for i in range(10,100):
    for j in range(i+1,100):
        if ( int(str(i)[1]) == 0 or int(str(j)[1])==0 ):
            continue
        elif (int(str(i)[0]) == int(str(j)[0])) and (int(str(i)[1])/int(str(j)[1]) == i/j):
            numeratorProduct = numeratorProduct*i
            denominatorProduct = denominatorProduct*j
        elif (int(str(i)[0]) == int(str(j)[1])) and (int(str(i)[1])/int(str(j)[0]) == i/j):
            numeratorProduct = numeratorProduct * i
            denominatorProduct = denominatorProduct * j
        elif (int(str(i)[1]) == int(str(j)[1])) and (int(str(i)[0])/int(str(j)[0]) == i/j):
            numeratorProduct = numeratorProduct * i
            denominatorProduct = denominatorProduct * j
        elif (int(str(i)[1]) == int(str(j)[0])) and (int(str(i)[0])/int(str(j)[1]) == i/j):
            numeratorProduct = numeratorProduct * i
            denominatorProduct = denominatorProduct * j

greatestCommonDivisor = math.gcd(numeratorProduct,denominatorProduct)
print(int(denominatorProduct/greatestCommonDivisor))