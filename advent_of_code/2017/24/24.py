#!/usr/bin/env python3


input = open('input').read()

cmps = []
for line in input.split('\n'):
    if line == '':
        continue
    a, b = [int(w) for w in line.split('/')]
    cmps.append((a, b))


def bb(k, cidx):
    m = 0
    for idx in cidx:
        a, b = cmps[idx]
        if a == k:
            pass
        elif b == k:
            a, b = b, a
        else:
            continue
        v = bb(b, cidx - {idx})
        m = max(m, v + a + b)
    return m


def bb2(k, cidx):
    m = (0, 0)
    for idx in cidx:
        a, b = cmps[idx]
        if a == k:
            pass
        elif b == k:
            a, b = b, a
        else:
            continue
        l, v = bb2(b, cidx - {idx})
        m = max(m, (l + 1, v + a + b))
    return m


print(bb(0, set(range(len(cmps)))))
print(bb2(0, set(range(len(cmps)))))
