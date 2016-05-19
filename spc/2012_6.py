#!/usr/bin/env python3

from pphelp import *

cnt = {}
def f(k, cn=0, co=0, stack=[]):
    s = len(stack)
    if cn == k and s == 1:
        res = stack[0]
        cnt[res] = cnt.get(res, 0) + 1
        return

    if cn < k:
        for i in range(1, 16):
            stacktmp = stack + [sp.sympify(i)]
            f(k, cn+1, co, stacktmp)

    if co < k-1 and s >= 2:
        a = stack[-2]
        b = stack[-1]

        stacktmp = stack[:-1]
        stacktmp[-1] = a + b
        f(k, cn, co+1, stacktmp)

        stacktmp = stack[:-1]
        stacktmp[-1] = a - b
        f(k, cn, co+1, stacktmp)

        stacktmp = stack[:-1]
        stacktmp[-1] = a * b
        f(k, cn, co+1, stacktmp)

        if (b != 0):
            stacktmp = stack[:-1]
            stacktmp[-1] = a / b
            f(k, cn, co+1, stacktmp)


f(4)
print(cnt[24])

m = 0;
mk = None
for k in cnt:
    if cnt[k] > m:
        m = cnt[k]
        mk = k

print('%d %d' % (mk, m))

