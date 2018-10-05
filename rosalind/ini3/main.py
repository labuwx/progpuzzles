#!/usr/bin/env python3

from sys import argv


ds = open(argv[1]).read()
s, a, b, c, d = ds.split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

ss = s[a:b+1] + ' ' + s[c:d+1]

print(ss)
