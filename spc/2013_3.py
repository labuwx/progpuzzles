#!/usr/bin/env python3

from pphelp import *

n = 5000
m = 500

a = [[1] * n] * n
a = np.matrix(a, dtype=np.int64)

t = [[0] * i + [1] * m + [0] * (n - m - i) if n - m >= i else [0] * n for i in range(n)]
t = np.matrix(t, dtype=np.int64)

res = t * a * t.transpose()

maxi = res.argmax()
max = res.item(maxi)

print(np.unravel_index(maxi, (n, n)))
print(max)
