#!/usr/bin/env python3

from pphelp import *


for n in it.count(285 + 1):
    k = triangle_num(n)
    if is_pentagonal(k) and is_hexagonal(k):
        # print(n)
        print(k)
        break
