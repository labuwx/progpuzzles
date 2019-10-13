#!/usr/bin/env python3


ml = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isleap(y):
    return not (y % 400) or bool(y % 100) and not (y % 4)


def issunday(d):
    return d % 7 == 5


s = 0
dc = 0
for y in range(1901, 2001):
    for m in range(0, 12):
        cl = 29 if (isleap(y) and m == 1) else ml[m]
        dc += cl
        s += 1 if issunday(dc) else 0


print(s)
