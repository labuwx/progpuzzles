#!/usr/bin/env python3

import itertools as it


def cell_score(p, grid_serial):
    x, y = p
    x, y = x+1, y+1
    rackid = x + 10
    plevel = (rackid * y + grid_serial) * rackid
    plevel = (plevel % 1000) // 100
    plevel -= 5
    return plevel


def mask_score(INT_T, p, mask_size):
    x, y = p
    score = INT_T[x+mask_size-1][y+mask_size-1]
    if x > 0:
        score -= INT_T[x-1][y+mask_size-1]
    if y > 0:
        score -= INT_T[x+mask_size-1][y-1]
    if x > 0 and y > 0:
        score += INT_T[x-1][y-1]
    return score


input = int(open('input').read().strip())
mask_size = 3
grid_size = 300

T = [
    [cell_score((x, y), input) for y in range(grid_size)]
    for x in range(grid_size)
]

INT_T = [[None] * grid_size for _ in range(grid_size)]
for x, y in it.product(range(grid_size), repeat=2):
    s = T[x][y]
    if x > 0:
        s += INT_T[x-1][y]
    if y > 0:
        s += INT_T[x][y-1]
    if x > 0 and y > 0:
        s -= INT_T[x-1][y-1]
    INT_T[x][y] = s

cmax = max(it.product(range(grid_size - mask_size), repeat=2), key=lambda p: mask_score(INT_T, p, mask_size))
s1 = r'%d,%d' % tuple(i+1 for i in cmax)

cmax2 = max((
        (p, s)
        for s in range(1, grid_size + 1)
        for p in it.product(range(grid_size - s), repeat=2)
    ),
    key=lambda X: mask_score(INT_T, X[0], X[1])
)
s2 = r'%d,%d,%d' % (cmax2[0][0]+1, cmax2[0][1]+1, cmax2[1])

print(s1)
print(s2)
