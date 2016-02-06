#!/usr/bin/env python3


def isnpan(k):
    k = str(k)
    k = ''.join(sorted(k))
    #print(k)


for k in range(1, 987654321):
    isnpan(k)
    if k%1000000 == 0:
        print(k)

