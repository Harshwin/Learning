f= open("names_p22.txt","r")
contents = f.read()
f.close()

namesListWithQotes = contents.split(',') #combine below 2 logic
# removing quotes
nameList1 = []
for names in namesListWithQotes:
    nameList1.append(names[1:-1])


nameList.sort() #sortingcust

print(namesScore(nameList))


def charTONumber(n):
    num = ord(n)

    if len(n)!=1:
        return 0

    else:
        return (num - 64 ) # as only capital letters are there

def namesScore(lst):
    score = 0
    count = 1
    for names in lst:
        score += sum(list(map(lambda X : charTONumber(X),names))) * count
        count += 1
    return score


def sortNames(lst):
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst






