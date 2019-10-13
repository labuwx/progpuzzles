#!/usr/bin/env python3


def ispan(n):
    return len(str(n)) == 9 and set(str(n)) == {
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
    }


def mul(k, l):
    res = ""
    for d in l:
        res += str(k * d)
    return int(res)


max = 0
l = [1]
for i in range(2, 10):
    l.append(i)
    for j in range(1, 99999):
        p = mul(j, l)
        if ispan(p) and p > max:
            max = p

print(max)
