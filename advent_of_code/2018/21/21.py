#!/usr/bin/env python3


def main():
    seen, d = set(), 0
    while d not in seen:
        seen.add(d)
        s2 = d
        c = d | 2 ** 16
        if len(seen) == 2:
            s1 = d

        d = 12670166
        while c > 0:
            d = ((d + (c % 256)) * 65899) % 2 ** 24
            c //= 256

    print(s1)
    print(s2)


main()
