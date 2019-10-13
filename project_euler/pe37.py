#!/usr/bin/env python3


def isprime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return n > 1


def lp(n):
    if n > 10:
        return isprime(n) and lp(int(str(n)[1:]))
    else:
        return isprime(n)


def rp(n):
    if n:
        return isprime(n) and rp(n // 10)
    else:
        return True


k = 0
s = 0
for n in range(10, 1000000):
    if lp(n) and rp(n):
        k += 1
        s += n
        print(str(k) + ': ' + str(n) + ' - ' + str(s))
