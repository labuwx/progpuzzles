#!/usr/bin/env python3

import re
from operator import lt, eq, gt


pattern_aunt = re.compile(r'Sue (?P<id>\d+)')
pattern_prop = re.compile(r'(?P<prop>\w+): (?P<value>\d+)')

props = {
    'children': (3, eq),
    'cats': (7, gt),
    'samoyeds': (2, eq),
    'pomeranians': (3, lt),
    'akitas': (0, eq),
    'vizslas': (0, eq),
    'goldfish': (5, lt),
    'trees': (3, gt),
    'cars': (2, eq),
    'perfumes': (1, eq),
}


def match(props, aunt, use_op=False):
    m = all(
        (props[prop][1] if use_op else eq)(val, props[prop][0])
        for prop, val in aunt.items()
    )
    return m


def main():
    input = open('input').read().strip().split('\n')
    aunts = {
        pattern_aunt.search(l)['id']: {
            m['prop']: int(m['value']) for m in pattern_prop.finditer(l)
        }
        for l in input
    }

    s1 = next(
        id for id, aunt_props in aunts.items() if match(props, aunt_props, use_op=False)
    )
    s2 = next(
        id for id, aunt_props in aunts.items() if match(props, aunt_props, use_op=True)
    )

    print(s1)
    print(s2)


main()
