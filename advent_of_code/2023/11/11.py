#!/usr/bin/env python3


def accsum(l):
    ll = [0] * (len(l) + 1)
    for i, x in enumerate(l):
        ll[i + 1] = ll[i] + x
    return ll


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = input.strip().split('\n')

    Xmax = len(input[0]) - 1
    Ymax = len(input) - 1

    g_x = [0] * (Xmax + 1)
    g_y = [0] * (Ymax + 1)
    empty_x = [1] * (Xmax + 1)
    empty_y = [1] * (Ymax + 1)
    for y, l in enumerate(input):
        for x, c in enumerate(l):
            if c == '.':
                continue
            g_x[x] += 1
            g_y[y] += 1
            empty_x[x] = 0
            empty_y[y] = 0

    g_x = accsum(g_x)
    g_y = accsum(g_y)
    empty_x = accsum(empty_x)
    empty_y = accsum(empty_y)

    manhattan = expansion = 0

    for x in range(Xmax + 1):
        n = (g_x[x + 1] - g_x[x]) * (g_x[x] + g_x[x + 1] - g_x[Xmax + 1])
        manhattan += x * n
        expansion += empty_x[x] * n

    for y in range(Ymax + 1):
        n = (g_y[y + 1] - g_y[y]) * (g_y[y] + g_y[y + 1] - g_y[Ymax + 1])
        manhattan += y * n
        expansion += empty_y[y] * n

    s1 = manhattan + (2 - 1) * expansion
    s2 = manhattan + (1000000 - 1) * expansion

    print(s1)
    print(s2)


main()
