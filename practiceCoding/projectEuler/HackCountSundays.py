
months = ['jan', 'feb', 'mar', 'apr', 'may', 'june', 'july', 'aug', 'sept', 'oct', 'nov', 'dec']
numberOfDaysInMonth = [31 ,28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]
daysInWeek = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
beginningDaysOfMonth1900 = ['mon' ,'thur', 'thur' ,'sun' ,'tue' ,'fri' ,'sun' ,'wed' ,'sat' ,'mon' ,'thur' ,'sat']
beginningDaysOfMonth1901 = ['tue' ,'fri' ,'fri' ,'mon' ,'wed' ,'sat' ,'mon' ,'thur' ,'sun' ,'tue' ,'fri' ,'sun']
def checkIfLeapYear(n):
    if n% 4 == 0 and ((n % 100 == 0 and n % 400 == 0) or n % 100 != 0):
        return True
    else:
        return False


def findDayofTheweek(y, m, k):  # zellers method to find day of a week
    if m == 1 or m == 2:
        D = int(str(y)[2:]) - 1
    else:
        D = int(str(y)[2:])
    m = (m - 3) % 12 + 1  # converting to zellers month index

    C = int(str(y)[:2])
    f = k + int((13 * m - 1) / 5) + D + int(D / 4) + int(C / 4) - 2 * C
    # print(m, k, D, C, f)
    return daysInWeek[int(f % 7)]


def countNumberOfStartingSundays(y1, m1, d1, y2, m2, d2):
    # currentDay = findDayofTheweek(y1,m1,d1)

    if d1 > 1:
        m1 = m1 + 1
    numberOfBeginningSundays = 0
    for year in range(y1, y2 + 1):
        beginningDaysOfThisYear = []
        if y1 == y2:
            beginningDaysOfThisYear = list(map(lambda x: findDayofTheweek(year, x, 1), range(m1, m2 + 1)))
        elif year == y2:
            beginningDaysOfThisYear = list(map(lambda x: findDayofTheweek(year, x, 1), range(1, m2 + 1)))
        elif year == y1:
            beginningDaysOfThisYear = list(map(lambda x: findDayofTheweek(year, x, 1), range(m1, 13)))

        else:
            beginningDaysOfThisYear = list(map(lambda x: findDayofTheweek(year, x, 1), range(1, 13)))

        numberOfBeginningSundays += beginningDaysOfThisYear.count('sun')

    return numberOfBeginningSundays


testCases = int(input().strip())
for a0 in range(testCases):
    [y1, m1, d1] = input().strip().split(' ')
    [y1, m1, d1] = [int(y1), int(m1), int(d1)]

    [y2, m2, d2] = input().strip().split(' ')
    [y2, m2, d2] = [int(y2), int(m2), int(d2)]

    noOfLeapYearsDivisibleBy400_1000 = [0 for i in range(y1, y2 + 1) if (i % 400 == 0 and i % 1000 == 0)].__len__()
    print(countNumberOfStartingSundays(y1, m1, d1, y2, m2, d2) - noOfLeapYearsDivisibleBy400_1000)



