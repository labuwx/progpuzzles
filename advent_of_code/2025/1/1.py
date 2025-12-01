#!/usr/bin/env python3


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = [(1 if x[0] == 'R' else -1, int(x[1:])) for x in input.strip().splitlines()]

    pos = 50
    s1 = s2 = 0
    for d, k in input:
        ppos = pos
        pos += k * d
        s2 += max(pos // 100, (-pos) // 100 + (ppos != 0))

        pos %= 100
        s1 += pos == 0

    print(s1)
    print(s2)


main()
