#!/usr/bin/env python3


def evolve(numbers, n):
    M = {}

    def f(x, k):
        if (x, k) in M:
            return M[(x, k)]

        if k == 0:
            res = 1
        elif x == 0:
            res = f(1, k - 1)
        elif len((sx := str(x))) % 2 == 0:
            mid = len(sx) // 2
            res = f(int(sx[:mid]), k - 1) + f(int(sx[mid:]), k - 1)
        else:
            res = f(2024 * x, k - 1)

        M[(x, k)] = res
        return res

    return sum(f(x, n) for x in numbers)


def main():
    input = open('input').read()
    # input = open('input_test').read()

    numbers = [int(x) for x in input.strip().split()]

    s1 = evolve(numbers, 25)
    s2 = evolve(numbers, 75)

    print(s1)
    print(s2)


main()
