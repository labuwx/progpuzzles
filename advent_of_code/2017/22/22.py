#!/usr/bin/env python3

from collections import defaultdict


def add(xs, ys):
    s = tuple(x+y for x, y in zip(xs, ys))
    return s

def turn(dt, dp):
    x, y = dp
    if dt == 'L':
        return (y, -x)
    elif dt == 'R':
        return (-y, x)
    elif dt == 'B':
        return (-x, -y)
    else:
        return (x, y)

turnmap = {
    0: 'L',
    1: ' ',
    2: 'R',
    3: 'B'
}


input = open('input').read()
input = [line for line in input.split('\n') if line != '']

grid = defaultdict(int)
yos, xos = len(input)//2, len(input[0])//2
for y, line in enumerate(input):
    for x, c in enumerate(line):
        grid[(x-xos, y-yos)] = (1 if c == '#' else 0)
grid_cp = grid.copy()


pos = (0, 0)
d = (0, -1)
cnt = 0
for _ in range(10000):
    c = grid[pos]
    d = turn('R' if bool(c) else 'L', d)
    grid[pos] = (c+1) % 2
    if grid[pos] == 1:
        cnt += 1
    pos = add(pos, d)
print(cnt)


grid = defaultdict(int, {p: 2*c for p, c in grid_cp.items()})
pos = (0, 0)
d = (0, -1)
cnt = 0
for _ in range(10000000):
    c = grid[pos]
    grid[pos] = (c+1) % 4
    if grid[pos] == 2:
        cnt += 1
    d = turn(turnmap[c], d)
    pos = add(pos, d)
print(cnt)





