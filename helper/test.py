#!/usr/bin/env python3

import time
from pphelp import *


# m = np.matrix([[1.0,2],[3,4]], dtype=object)
# m = np.matrix(np.random.randint(100000, size=(5, 5)), dtype=object)
# i = np.identity(m.shape[0], dtype=np.int64)
# n = 50000
#
# print(m)
#
# start = time.time()
# me = mexp(m, n)
# stop = time.time()
# print(me)
# print(stop - start)

# for i in range(10):
#    print(scp_rand(5, i+1))
#
# print(scp_rand(1000, 1000))

n = 5000000000000
n = 10
print(linrec([0, 1, 1], [1, 3], n - 1, 1234567))
