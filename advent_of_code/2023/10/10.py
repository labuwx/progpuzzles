#!/usr/bin/env python3


dirmap = {
    'F': {(0, 1), (1, 0)},
    'J': {(-1, 0), (0, -1)},
    'L': {(0, -1), (1, 0)},
    '7': {(-1, 0), (0, 1)},
    '-': {(-1, 0), (1, 0)},
    '|': {(0, -1), (0, 1)},
}


def tadd(a, b):
    return tuple(aa + bb for aa, bb in zip(a, b))


def main():
    input = open('input').read()
    # input = open('input_test_1').read()
    # input = open('input_test_2').read()
    # input = open('input_test_3').read()
    input = input.strip().split('\n')

    # find S
    for y, l in enumerate(input):
        for x, c in enumerate(l):
            pos = (x, y)
            if c == 'S':
                S = pos

    # build a graph
    G = {S: set()}
    for y, l in enumerate(input):
        for x, c in enumerate(l):
            pos = (x, y)
            if c in '.S':
                continue
            G[pos] = {tadd(pos, dir) for dir in dirmap[c]}
            for nb in G[pos]:
                if nb == S:
                    G[S].add(pos)

    # search graph
    pos, len_cyc, area = S, 0, 0
    prev = next(iter(G[S]))
    while pos != S or len_cyc == 0:
        next_pos = next(nb for nb in G[pos] if nb != prev)

        len_cyc += 1
        area += (next_pos[0] - prev[0]) * pos[1]

        prev, pos = pos, next_pos

    area = abs(area) // 2

    # len_cyc = edge + corner
    # inner = area - edge//2 - (corner-2)//2
    inner = area - (len_cyc - 2) // 2

    s1 = len_cyc // 2
    s2 = inner

    print(s1)
    print(s2)


main()
