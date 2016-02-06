#!/usr/bin/env python3

import json


with open('p042_words.txt') as fil:
    fc = fil.read()

fc = '[' + fc + ']'
words = json.loads(fc)


def istr(w):
    val = sum([ord(c) - 96 for c in w.lower()])
    val = 2*val
    for k in range(1, val):
        if k * (k+1) == val:
            return True
    return False


count = 0
for w in words:
    if istr(w):
        count += 1

print(count)

