#!/usr/bin/env python3


def check_pwd(n, two_match=False):
    n = [int(d) for d in str(n)]
    ndigit = len(n) == 6
    inc, ddigit = True, False
    for x, a, b, y in zip([None] + n, n, n[1:], n[2:] + [None]):
        inc &= a <= b
        ddigit |= a == b and not (two_match and (x == a or b == y))
    return ndigit and inc and ddigit


def main():
    input = open('input').read().strip()
    lmin, lmax = (int(x) for x in input.split('-'))

    s1 = s2 = 0
    for n in range(lmin, lmax + 1):
        s1 += check_pwd(n, two_match=False)
        s2 += check_pwd(n, two_match=True)

    print(s1)
    print(s2)


main()
