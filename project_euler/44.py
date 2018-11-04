#!/usr/bin/env python3

from pphelp import *

for i in range(1, 10000):
    pi = pentagonal_num(i)
    for j in range(i+1, i+10000):
        pj = pentagonal_num(j)
        if pi%2 != pj%2:
            continue
        pa = (pi + pj) // 2
        pb = (pj - pi) // 2
        if is_pentagonal(pa) and is_pentagonal(pb):
            # print(i, j, pi)
            print(pi)

