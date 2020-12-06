#!/usr/bin/env python3

from collections import deque


def open_space(pos):
    x, y = pos
    n = x * x + 3 * x + 2 * x * y + y + y * y
    n += FAVN
    nbits = f'{n:b}'.count('1')
    isopen = nbits % 2 == 0

    return isopen


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def adj(pos):
    adj = (cadd(pos, d) for d in dirs)
    return (p for p in adj if min(p) >= 0)


def main():
    global FAVN
    input = int(open('input').read().strip())
    FAVN = input
    target = (31, 39)
    start_pos = (1, 1)
    max_steps = 50

    q = deque([(start_pos, 0)])
    reached = {start_pos}
    s1, s2 = None, 0
    while q:
        pos, dist = q.popleft()
        if pos == target:
            s1 = dist
        if dist <= max_steps:
            s2 += 1
        if s1 != None and dist > max_steps:
            break

        new_adj = [p for p in adj(pos) if open_space(p) and p not in reached]
        reached.update(new_adj)
        q.extend((p, dist + 1) for p in new_adj)

    print(s1)
    print(s2)


main()
