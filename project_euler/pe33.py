def nt(a, b):
    a1 = a // 10
    a2 = a % 10
    b1 = b // 10
    b2 = b % 10

    if (a1 == b2) and (a2 * b == a * b1):
        return True

    if (a2 == b1) and (a1 * b == a * b2):
        return True

    if (a1 == b1) and (a2 * b == a * b2):
        return True

    if (a2 == b2 != 0) and (a1 * b == a * b1):
        return True

    return False


fl = []

for a in range(10, 99):
    for b in range(a + 1, 100):
        if nt(a, b):
            fl.append((a, b))

a = reduce(lambda prod, x: prod * x[0], fl, 1)
b = reduce(lambda prod, x: prod * x[1], fl, 1)

print(fl)
print(a)
print(b)
