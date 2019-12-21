#!/usr/bin/env python3


def main():
    input = open('input').read().strip()
    steps = [1 if c == '(' else -1 for c in input]

    s1, s2 = 0, None
    for i, step in enumerate(steps):
        s1 += step
        if s2 == None and s1 < 0:
            s2 = i + 1

    print(s1)
    print(s2)


main()
