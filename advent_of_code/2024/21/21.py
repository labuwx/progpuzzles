#!/usr/bin/env python3

from heapq import heappush, heappop
import itertools as it


UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)
directions = {UP: '^', DOWN: 'v', LEFT: '<', RIGHT: '>'}


def read_kp(kp_text):
    kp = {}
    for y, l in enumerate(kp_text.strip().splitlines()):
        for x, c in enumerate(l.strip()):
            if c != 'X':
                kp[c] = (x, y)
    return kp


num_kp = '''
789
456
123
X0A
'''
num_kp = read_kp(num_kp)

dir_kp = '''
X^A
<v>
'''
dir_kp = read_kp(dir_kp)


def tadd(a, b):
    return tuple(ax + bx for ax, bx in zip(a, b))


def dijkstra(G, start, dst):
    GG = {pos: x for x, pos in G.items()}

    q = [(0, False, start, 'A')]
    reached = {}
    while q:
        dist, pushed, u, bp = heappop(q)

        key = (u, pushed, bp)
        if key in reached:
            continue
        else:
            reached[key] = dist

        if pushed:
            continue

        heappush(q, (dist + dst[bp, 'A'], True, u, 'A'))

        pos = G[u]
        for dir, bc in directions.items():
            if v := GG.get(tadd(pos, dir)):
                heappush(q, (dist + dst[(bp, bc)], False, v, bc))

    return {u: d for (u, pushed, _), d in reached.items() if pushed}


def kp_iter(dst, n):
    for _ in range(n):
        dst = {
            (u, v): d
            for u in dir_kp.keys()
            for v, d in dijkstra(dir_kp, u, dst).items()
        }

    dst = {
        (u, v): d for u in num_kp.keys() for v, d in dijkstra(num_kp, u, dst).items()
    }
    return dst


def compsum(dst, codes):
    s = 0
    for code in codes:
        l, prev = 0, 'A'
        for x in code:
            l += dst[(prev, x)]
            prev = x
        s += l * int(code[:-1])
    return s


def main():
    input = open('input').read()
    # input = open('input_test').read()
    codes = input.strip().splitlines()

    # dst[(u,v)] = number of level 0 button presses needed
    # to press v on the current level if the last action was pressing u on the current level
    dst0 = {(u, v): 1 for u, v in it.product(dir_kp.keys(), repeat=2)}

    s1 = compsum(kp_iter(dst0, 2), codes)
    s2 = compsum(kp_iter(dst0, 25), codes)

    print(s1)
    print(s2)


main()
