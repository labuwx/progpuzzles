#!/usr/bin/env python3

import re


def dance(mem, moves, n=1):
    mem = mem.copy()
    cache = [tuple(mem)]
    for k in range(n):
        for op, a1, a2 in moves:
            if op == 's':
                mem = mem[-a1:] + mem[:-a1]
            elif op == 'x':
                mem[a1], mem[a2] = mem[a2], mem[a1]
            elif op == 'p':
                i1, i2 = mem.index(a1), mem.index(a2)
                mem[i1], mem[i2] = mem[i2], mem[i1]

        m2c = tuple(mem)
        if m2c in cache:
            cs = cache.index(m2c)
            l = len(cache) - cs
            mem = cache[(n - cs) % l + cs]
            break
        else:
            cache.append(m2c)

    return mem


input = open('input').read()
input = re.sub(r'\n', '', input).split(',')

moves = []
for cmd in input:
    m = re.match(r'^(?P<op>[sxp])(?P<a1>\w+)(/(?P<a2>\w+))?$', cmd)
    op, a1, a2 = m.group('op'), m.group('a1'), m.group('a2')
    if op == 's':
        a1 = int(a1)
    elif op == 'x':
        a1, a2 = int(a1), int(a2)
    moves.append((op, a1, a2))


mem = [chr(ord('a') + i) for i in range(16)]

res1 = ''.join(dance(mem, moves))
res2 = ''.join(dance(mem, moves, 1000000000))

print(res1)
print(res2)
