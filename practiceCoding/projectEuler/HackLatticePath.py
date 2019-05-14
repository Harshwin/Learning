#!/bin/python3

import math

t = int(input().strip())
for a0 in range(t):
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]

    print(int((math.factorial(n + m) // (math.factorial(n) * math.factorial(m))) % 1000000007))
