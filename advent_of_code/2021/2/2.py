#!/usr/bin/env python3

# TODO: rewrite with pattern matching

def main():
    input = open('input').read().strip()
    input = [(l[0], int(l[1])) for l in (l.split() for l in input.split('\n'))]

    horp, aim, depth1, depth2 = 0, 0, 0, 0
    for dir, n in input:
        if dir == 'forward':
            horp += n
            depth2 += aim * n
        elif dir == 'down':
            depth1 += n
            aim += n
        elif dir == 'up':
            depth1 -= n
            aim -= n
        else:
            assert False

    s1 = horp * depth1
    s2 = horp * depth2

    print(s1)
    print(s2)


main()
