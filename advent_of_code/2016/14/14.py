#!/usr/bin/env python3

from collections import deque
import hashlib
import itertools as it
import re


def md5(salt, index, stretch=False):
    n = 2017 if stretch else 1
    hash = salt + str(index)

    for _ in range(n):
        hash = hashlib.new('md5', hash.encode('ascii')).hexdigest()

    return hash


key_pattern = re.compile(r'(.)\1{2}')
ver_pattern = re.compile(r'(.)\1{4}')


def find_key(salt, stretch=False):
    keys_needed = 64
    candidates = deque()
    keys, keys_max = [], -1
    for i in it.count():
        if candidates and candidates[0][0] < i - 1000:
            candidates.popleft()
        if len(keys) >= keys_needed and (not candidates or candidates[0][0] > keys_max):
            break

        hash = md5(salt, i, stretch)
        m = key_pattern.search(hash)
        if m == None:
            continue

        ver_digits = {ds[0] for ds in ver_pattern.findall(hash)}

        candidates.append(None)
        while candidates[0] != None:
            idx, d = candidates[0]
            if d in ver_digits:
                candidates.popleft()
                if len(keys) < keys_needed or idx < keys_max:
                    keys.append(idx)
                    keys_max = max(keys_max, idx)
            else:
                candidates.rotate(-1)
        candidates.popleft()

        if len(keys) < keys_needed:
            key_digit = m[0][0]
            candidates.append((i, key_digit))

    return sorted(keys)[keys_needed - 1]


def main():
    input = open('input').read().strip()
    salt = input

    s1 = find_key(salt)
    s2 = find_key(salt, stretch=True)

    print(s1)
    print(s2)


main()
