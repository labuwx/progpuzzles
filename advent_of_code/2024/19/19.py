#!/usr/bin/env python3


def match(towels, pattern):
    M = [None] * len(pattern) + [1]

    def f(j):
        if M[j] is not None:
            return M[j]

        s = 0
        for t in towels:
            if pattern[j:].startswith(t):
                s += f(j + len(t))

        M[j] = s
        return s

    return f(0)


def main():
    input = open('input').read()
    # input = open('input_test').read()

    input = input.strip().split('\n\n')
    towels = input[0].split(', ')
    patterns = input[1].splitlines()

    matches = [match(towels, p) for p in patterns]
    s1 = sum(m > 0 for m in matches)
    s2 = sum(matches)

    print(s1)
    print(s2)


main()
