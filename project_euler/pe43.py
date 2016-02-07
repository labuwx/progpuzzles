#!/usr/bin/env python3


ps = [2, 3, 5, 7, 11, 13, 17]


def hasprop(n):
    for k in range(7):
        sl =int(str(n)[k+1 : k+4])
        if sl % ps[k]:
            return False

    return True


sum = 0
def check(l):
    global sum
    n = int(''.join([str(k) for k in l]))
    if hasprop(n):
        print(n)
        sum += n


def forperm(l, f, t=[]):
    if l:
        for i in range(len(l)):
            p = t[:]
            p.append(l[i])
            l2 = l[:]
            del l2[i]
            forperm(l2, f, p)
    else:
        f(t)


l = list(range(0, 10))
forperm(l, check)

print(sum)

