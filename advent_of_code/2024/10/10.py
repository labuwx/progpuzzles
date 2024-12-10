#!/usr/bin/env python3


directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def tadd(a, b):
    return tuple(ax + bx for ax, bx in zip(a, b))


def main():
    input = open('input').read()
    # input = open('input_test').read()

    map = {
        (x, y): int(c)
        for y, l in enumerate(input.strip().splitlines())
        for x, c in enumerate(l)
    }

    levels = [[] for _ in range(9 + 1)]
    for pos, k in map.items():
        levels[k].append(pos)

    reach_cnt_1 = {pos: {pos} if k == 9 else set() for pos, k in map.items()}
    reach_cnt_2 = {pos: int(k == 9) for pos, k in map.items()}

    for level in range(9, 0, -1):
        for pos in levels[level]:
            for dir in directions:
                if (npos := tadd(pos, dir)) in map and map[npos] == level - 1:
                    reach_cnt_1[npos] |= reach_cnt_1[pos]
                    reach_cnt_2[npos] += reach_cnt_2[pos]

    s1 = sum(len(reach_cnt_1[pos]) for pos in levels[0])
    s2 = sum(reach_cnt_2[pos] for pos in levels[0])

    print(s1)
    print(s2)


main()
