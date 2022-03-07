#!/usr/bin/env python3

import itertools as it
import re


def parse_input(input):
    pattern = r'target area: x=(?P<xmin>-?\d+)\.\.(?P<xmax>-?\d+), y=(?P<ymin>-?\d+)\.\.(?P<ymax>-?\d+)'
    m = re.match(pattern, input)
    return ((int(m['xmin']), int(m['xmax'])), (int(m['ymin']), int(m['ymax'])))


def genpos(v):
    vx, vy = v
    x = y = 0
    while True:
        yield x, y
        x += vx
        y += vy
        vy -= 1
        vx -= 1 if vx > 0 else 0


def simul(v, target):
    (tx, tX), (ty, tY) = target
    ymax = 0
    for pos in genpos(v):
        x, y = pos
        ymax = max(ymax, y)
        if x in range(tx, tX + 1) and y in range(ty, tY + 1):
            return ymax
        if tX < x or y < ty:
            return None


def search(target):
    ymax = 0
    good_v_cnt = 0
    vy_bound = -target[1][0]
    for v in it.product(range(target[0][1] + 1), range(-vy_bound, vy_bound + 1)):
        if (ym := simul(v, target)) is not None:
            good_v_cnt += 1
            ymax = max(ymax, ym)
    return ymax, good_v_cnt


def main():
    input = open('input').read().strip()
    # input = open('input_test').read().strip()

    target = parse_input(input)
    s1, s2 = search(target)

    print(s1)
    print(s2)


main()
