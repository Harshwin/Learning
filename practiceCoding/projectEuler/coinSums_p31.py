# check for small values
count = 0
[1,2] = 5
for x1 in range(0,4):
    for x2 in range(0,12):
        if x1*1 + x2*2 == 5 :
            count += 1

print(count)


# count = 0
# for x1 in range(0,201):
#     for x2 in range(0,101):
#         for x5 in range(0,41):
#             for x10 in range(0,21):
#                 for x20 in range(0,11):
#                     for x100 in range(0,2):
#                         if x1*1 + x2*2 + x5*5 + x10*10 + x20*20 + x100*100 == 200:
#                             count += 1
#
# print(count)


# def countNumberOfWaysWeGetChange(index, value):
#     denominationlist = [1, 2, 5, 10, 20, 50, 100, 200]
#     for i in range(0,value/denominationlist[0]):
#         if (value - i*denominationlist[0])%b == 0:
#             count += 1
#         else:
#             value - i*denominationlist[0] - i*denominationlist[]