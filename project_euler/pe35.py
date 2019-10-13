def isprime(l):
    n = tonum(l)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def tonum(l):
    return reduce(lambda acc, x: 10 * acc + x, l[::-1], 0)


def digits(n):
    dlist = []

    while n:
        dlist.append(n % 10)
        n //= 10

    return dlist


def shiftnum(k):
    n = list(k)
    tmp = n[0]
    del n[0]
    n.append(tmp)

    return n


def iscp(n):
    n = digits(n)
    k = list(n)

    b = isprime(k)
    k = shiftnum(k)

    while (k != n) and b:
        b = isprime(k)
        k = shiftnum(k)

    return b


cpl = []

for n in range(2, 1000000):
    if iscp(n):
        print(n)
        cpl.append(n)

print(len(cpl))
