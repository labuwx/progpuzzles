#!/usr/bin/env python3


def main():
    input = open('input').read().strip()
    input = [(l[0], int(l[1])) for l in (l.split() for l in input.split('\n'))]

    horp, aim, depth1, depth2 = 0, 0, 0, 0
    for l in input:
        match l:
            case ('forward', n):
                horp += n
                depth2 += aim * n
            case ('down', n):
                depth1 += n
                aim += n
            case ('up', n):
                depth1 -= n
                aim -= n
            case _:
                assert False

    s1 = horp * depth1
    s2 = horp * depth2

    print(s1)
    print(s2)


main()
