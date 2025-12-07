#!/usr/bin/env python3


def main():
    input = open('input').read()
    # input = open('input_test').read()

    input = input.strip().splitlines()

    s1, s2 = 0, 1
    v = [1 if c == 'S' else 0 for c in input[0]]
    for l in input[1:]:
        for x, c in enumerate(l):
            if c == '^' and v[x] > 0:
                s1 += 1
                s2 += v[x]
                v[x - 1] += v[x]
                v[x + 1] += v[x]
                v[x] = 0

    print(s1)
    print(s2)


main()
