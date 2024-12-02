#!/usr/bin/env python3


def sign(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1


def checkd(x, y, t):
    b = 1 <= abs(y - x) <= 3 and t * x <= t * y
    tt = sign(y - x)
    return b, tt


def is_safe(l, allow_damp=False):
    M = [(None, False, 0)]

    for y in l:
        MM, goodY = [], set()
        for x, dampened, t in M:
            if not dampened and allow_damp:
                MM.append((x, True, t))

            if x is None:
                goodY.add((dampened, t))
            else:
                b, tt = checkd(x, y, t)
                if b:
                    goodY.add((dampened, tt))

        MM.extend((y, dampened, tt) for dampened, tt in goodY)

        if not MM:
            return False
        M = MM

    return True


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = [[int(x) for x in l.split()] for l in input.strip().splitlines()]

    s1 = sum(is_safe(l, allow_damp=False) for l in input)
    s2 = sum(is_safe(l, allow_damp=True) for l in input)

    print(s1)
    print(s2)


main()
