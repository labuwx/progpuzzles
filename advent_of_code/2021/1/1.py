#!/usr/bin/env python3


def ninc(l):
    return sum(d2 > d1 for d1, d2 in zip(l, l[1:]))


def main():
    input = open('input').read()
    input = [int(x) for x in input.split()]

    s1 = ninc(input)
    s2 = ninc([sum(w) for w in zip(input, input[1:], input[2:])])

    print(s1)
    print(s2)


main()
