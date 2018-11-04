#!/usr/bin/env python3

from pphelp import *


for n in it.count(2):
    if all(len(factors(n+k)) == 4 for k in range(4)):
        print(n)
        break
