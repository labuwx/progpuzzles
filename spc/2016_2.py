#!/usr/bin/env python3

from pphelp import *


N = 500000


ds = {k: divsum(k) for k in range(2, N+1)}

nan = set()

for x in range(2, N+1):
    if x in nan:
        continue
    k = ds[x]
    terms = set()
    while 1<=k and k<=N and k not in terms:
        terms.add(k)
        if k==1 or k==x:
            nan.add(x)
            nan.update(terms)
            break
        k = ds[k]




print(sum(nan))
#pprint(nan)
#print(divsum(1))

