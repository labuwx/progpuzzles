#!/usr/bin/env python3

from collections import Counter
from itertools import zip_longest

input = open('input').read().split()
input = list(map(list, zip_longest(*input)))

msg = ''
msg2 = ''
for line in input:
    cnt = Counter(line).most_common()
    msg += cnt[0][0]
    msg2 += cnt[-1][0]

print(msg)
print(msg2)
