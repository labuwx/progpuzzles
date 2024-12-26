#!/usr/bin/env python3


UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)
directions = {'^': UP, 'v': DOWN, '<': LEFT, '>': RIGHT}


def tadd(a, b, t=1):
    return tuple(ax + t * bx for ax, bx in zip(a, b))


def movebox(map, pos, dir, dryrun):
    if map[pos] == ']':
        pos = tadd(pos, LEFT)

    n1pos = tadd(pos, dir, 1)
    n2pos = tadd(pos, dir, 2)
    n1Rpos = tadd(n1pos, RIGHT)
    posR = tadd(pos, RIGHT)

    if dir == RIGHT:
        if n2pos not in map:
            r = False
        elif map[n2pos] == '.':
            r = True
        elif map[n2pos] == '[':
            r = movebox(map, n2pos, dir, dryrun)

        if not dryrun:
            map[pos] = '.'
            map[n1pos], map[n2pos] = '[]'

    elif dir == LEFT:
        if n1pos not in map:
            r = False
        elif map[n1pos] == '.':
            r = True
        elif map[n2pos] == '[':
            r = movebox(map, n2pos, dir, dryrun)

        if not dryrun:
            map[posR] = '.'
            map[n1pos], map[pos] = '[]'

    else:
        r = (n1pos in map) and (n1Rpos in map)
        if r:
            if map[n1pos] == '.' and map[n1Rpos] == '.':
                r = True
            elif map[n1pos] == '[':
                r = movebox(map, n1pos, dir, dryrun)
            elif map[n1pos] == ']' and map[n1Rpos] == '.':
                r = movebox(map, n1pos, dir, dryrun)
            elif map[n1pos] == ']' and map[n1Rpos] == '[':
                r = movebox(map, n1pos, dir, dryrun) and movebox(
                    map, n1Rpos, dir, dryrun
                )
            elif map[n1pos] == '.' and map[n1Rpos] == '[':
                r = movebox(map, n1Rpos, dir, dryrun)

        if not dryrun:
            map[pos], map[posR] = '..'
            map[n1pos], map[n1Rpos] = '[]'

    return r


def main():
    input = open('input').read()
    # input = open('input_test_1').read()
    # input = open('input_test_2').read()
    input = input.strip().split('\n\n')

    map = {}
    for y, l in enumerate(input[0].strip().splitlines()):
        for x, c in enumerate(l):
            pos = (x - 1, y - 1)
            if c != '#':
                map[pos] = c
            if c == '@':
                S = pos
                map[pos] = '.'

    map2 = {}
    for (x, y), c in map.items():
        if c == '.':
            map2[(2 * x, y)] = '.'
            map2[(2 * x + 1, y)] = '.'
        else:
            map2[(2 * x, y)] = '['
            map2[(2 * x + 1, y)] = ']'

    steps = [directions[s] for s in input[1] if s != '\n']

    pos = S
    for step in steps:
        npos = tadd(pos, step)
        if npos not in map:
            continue

        nnpos = npos
        while nnpos in map:
            if map[nnpos] == '.':
                map[npos], map[nnpos] = map[nnpos], map[npos]
                break
            nnpos = tadd(nnpos, step)

        if map[npos] == '.':
            pos = npos
            continue

    s1 = sum((x + 1) + 100 * (y + 1) for (x, y), c in map.items() if c == 'O')

    pos = (2 * S[0], S[1])
    for step in steps:
        npos = tadd(pos, step)

        if map2.get(npos) == '.':
            pos = npos
        elif map2.get(npos, '%') in '[]' and movebox(map2, npos, step, True):
            pos = npos
            movebox(map2, npos, step, False)

    s2 = sum((x + 2) + 100 * (y + 1) for (x, y), c in map2.items() if c == '[')

    print(s1)
    print(s2)


main()
