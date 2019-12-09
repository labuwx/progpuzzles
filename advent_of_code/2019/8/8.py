#!/usr/bin/env python3

import numpy as np
import itertools as it


height, width = 6, 25


def overlay(p):
    i = np.where(p != 2)[0][0]
    return p[i]


def imgprint(img):
    for l in img:
        r = ''.join('*' if p == 1 else ' ' for p in l)
        print(r)


def main():
    input = list(reversed([int(d) for d in open('input').read().strip()]))

    img = np.zeros((len(input) // width // height, height, width), dtype=int)
    for l, y, x in it.product(img, range(height), range(width)):
        l[(y, x)] = input.pop()

    l1 = max(img, key=np.count_nonzero)
    s1 = np.count_nonzero(l1 == 1) * np.count_nonzero(l1 == 2)
    print(s1)
    img_red = np.apply_along_axis(overlay, 0, img)
    imgprint(img_red)


main()
