#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
ns = [int(x) for x in ds.split()]

es = [1, 1, 1, 3 / 4, 1 / 2, 0]

exp = sum(a * b for a, b in zip(ns, es)) * 2  # numpy.dot

print(exp)
