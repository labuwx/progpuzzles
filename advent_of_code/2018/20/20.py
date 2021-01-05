#!/usr/bin/env python3

from collections import deque, defaultdict
import re


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def parse(rgx):
    tokens = []

    plevel, s = 0, ''
    for i, c in enumerate(rgx):
        if c == '(':
            if plevel == 0:
                tokens.append(s)
                s = ''
                subs = []
            else:
                s += c
            plevel += 1
        elif c == ')':
            plevel -= 1
            if plevel == 0:
                subs.append(parse(s))
                s = ''
                tokens.append(subs)
            else:
                s += c
        elif c == '|':
            if plevel == 1:
                subs.append(parse(s))
                s = ''
            else:
                s += c
        else:
            s += c
    tokens.append(s)

    return tokens


dirmap = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}


def explore(tokens, pos, map=None):
    map = defaultdict(set) if map is None else map
    if len(tokens) == 0:
        return map

    t = tokens[0]
    if isinstance(t, str):
        for c in t:
            np = cadd(pos, dirmap[c])
            map[pos].add(np)
            map[np].add(pos)
            pos = np
        explore(tokens[1:], pos, map)
    elif [''] in t:
        for p in t:
            explore(p, pos, map)
        explore(tokens[1:], pos, map)
    else:
        for p in t:
            explore(p + tokens[1:], pos, map)

    return map


def main():
    input = open('input').read().strip()[1:-1]
    dist_min = 1000

    tokens = parse(input)
    map = explore(tokens, (0, 0))

    s1 = s2 = 0
    q = deque([((0, 0), 0)])
    seen = set()
    while q:
        pos, d = q.popleft()

        if pos in seen:
            continue
        else:
            seen.add(pos)

        s1 = max(s1, d)
        s2 += d >= dist_min

        q.extend((np, d + 1) for np in map[pos])

    print(s1)
    print(s2)


main()
