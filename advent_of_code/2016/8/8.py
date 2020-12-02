#!/usr/bin/env python3

import numpy as np
import re


pattern = re.compile(
    r'^ (?P<cmd>rect|rotate\ row|rotate\ column)\ \D* (?P<v1>\d+) \D+ (?P<v2>\d+) $',
    flags=re.VERBOSE,
)


def draw(screen):
    for l in screen.T:
        print(''.join('#' if x else ' ' for x in l))


def main():
    dim = (50, 6)
    input = open('input').read().strip().split('\n')
    # dim = (7, 3)
    # input = open('input_test').read().strip().split('\n')

    instr = [
        (m.group('cmd'), int(m.group('v1')), int(m.group('v2')))
        for m in (pattern.match(l) for l in input)
    ]

    screen = np.zeros(dim, dtype=int)

    for cmd, v1, v2 in instr:
        if cmd == 'rect':
            screen[:v1, :v2] = 1
        elif cmd == 'rotate row':
            screen[:, v1] = np.roll(screen[:, v1], v2)
        else:  # 'rotate column'
            screen[v1, :] = np.roll(screen[v1, :], v2)

    s1 = np.sum(screen)

    print(s1)
    draw(screen)


main()
