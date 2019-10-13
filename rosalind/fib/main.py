#!/usr/bin/env python3

from functools import lru_cache

from bioinf_common import *


@lru_cache()
def fib(n, k):
    if n <= 2:
        return 1
    return k * fib(n - 2, k) + fib(n - 1, k)


ds = get_dataset()
n, k = (int(x) for x in ds.split())

print(fib(n, k))
