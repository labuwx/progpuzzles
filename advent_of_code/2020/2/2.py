#!/usr/bin/env python3

import re


pattern = re.compile(r'^(?P<fmin>\d+)-(?P<fmax>\d+) (?P<char>\w): (?P<pwd>\w+)$')


def main():
    input = open('input').read().strip().split('\n')

    db = [
        (
            (int(m.group('fmin')), int(m.group('fmax'))),
            m.group('char'),
            m.group('pwd'),
        )
        for m in (pattern.match(l) for l in input)
    ]

    s1 = sum(fmin <= pwd.count(char) <= fmax for (fmin, fmax), char, pwd in db)
    s2 = sum(
        (pwd[pos1 - 1] == char) != (pwd[pos2 - 1] == char)
        for (pos1, pos2), char, pwd in db
    )

    print(s1)
    print(s2)


main()
