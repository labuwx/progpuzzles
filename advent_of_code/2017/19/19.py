#!/usr/bin/env python3


def add(xs, ys):
    s = tuple(x+y for x, y in zip(xs, ys))
    return s

def inv(xs):
    return tuple(-x for x in xs)

dimap = {
    'D': (0, 1),
    'U': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}

input = open('input').read()

map = {}
y = 0
for line in input.split('\n'):
    if line == '': continue
    x = 0
    for c in line:
        if c != ' ':
            map[(x, y)] = c
        x += 1
    y += 1

pos = next((x,y) for (x, y), c in map.items() if y == 0 and c == '|')
di = dimap['D']
path, steps = '', 0
while True:
    steps += 1
    pos = add(pos, di)
    c = map.get(pos, None)
    if c == None: break
    if c not in ['-', '|', '+']:
        path += c
    if c == '+':
        for dc, di2 in dimap.items():
            if di2 == inv(di): continue
            c2 = map.get(add(pos, di2), None)
            if (dc in ['L', 'R'] and c2 == '-') or (dc in ['U', 'D'] and c2 == '|'):
                di = di2
                break

print(path)
print(steps)
