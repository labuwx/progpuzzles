#!/usr/bin/env python3

from collections import defaultdict


dirmap = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}


dimap_verb = {'D': (0, 1), 'U': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


def add(xs, ys):
    s = tuple(x + y for x, y in zip(xs, ys))
    return s


def mult(xs, c):
    s = tuple(c * x for x in xs)
    return s


def turn(d, t):
    t %= 3
    if t == 0:
        nd = (d[1], -d[0])
    elif t == 1:
        nd = d
    else:
        nd = (-d[1], d[0])
    return nd


def curv(d, crv):
    if d[0]:
        if crv == '/':
            nd = dimap_verb['U']
        else:
            nd = dimap_verb['D']
        nd = mult(nd, d[0])
    else:
        if crv == '/':
            nd = dimap_verb['L']
        else:
            nd = dimap_verb['R']
        nd = mult(nd, d[1])
    return nd


input = open('input').read()

map = {}
y = 0
for line in input.split('\n'):
    if line == '':
        continue
    x = 0
    for c in line:
        if c != ' ':
            map[(x, y)] = c
        x += 1
    y += 1

carts = []
for p, d in list(map.items()):
    if d not in dirmap.keys():
        continue
    carts.append((p, dirmap[d], 0))
    map[p] = '-' if d in '<>' else '|'

crashed = set()
cartmap = defaultdict(lambda: None, {p: c for c, (p, _, _) in enumerate(carts)})
while len(crashed) != len(carts) - 1:
    order = sorted(range(len(carts)), key=lambda c: (carts[c][0][1], carts[c][0][0]))
    for c in order:
        if c in crashed:
            continue
        pp, d, t = carts[c]
        p = add(pp, d)
        cartmap[pp] = None
        if cartmap[p] != None:
            if len(crashed) == 0:
                fcrash = p
            crashed |= {c, cartmap[p]}
            cartmap[p] = None
            if len(crashed) == len(carts) - 1:
                break
            else:
                continue
        cartmap[p] = c
        cell = map[p]
        if cell == '+':
            d = turn(d, t)
            t += 1
        elif cell in '\/':
            d = curv(d, cell)
        carts[c] = (p, d, t)
s1 = '%d,%d' % fcrash
rem = next(iter(set(range(len(carts))) - crashed))
prem, pd = carts[rem][:2]
s2 = '%d,%d' % add(prem, pd)

print(s1)
print(s2)
