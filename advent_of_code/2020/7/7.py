#!/usr/bin/env python3

from collections import deque
import re

pattern_container = re.compile(r'(?P<color>\w+ \w+) bags contain')
pattern_contained = re.compile(r'(?P<num>\d+) (?P<color>\w+ \w+) bag')


def count_container(bags, color):
    q = deque([color])
    seen = set()
    while q:
        color = q.popleft()
        adj = {
            bag for bag, inside in bags.items() if bag not in seen and color in inside
        }
        q.extend(adj)
        seen.update(adj)
    return len(seen)


def count_contained(bags, color):
    n_inside = sum(n + n * count_contained(bags, bag) for bag, n in bags[color].items())
    return n_inside


def main():
    input = open('input').read().strip().split('\n')
    bags = {
        pattern_container.search(l)['color']: {
            m['color']: int(m['num']) for m in pattern_contained.finditer(l)
        }
        for l in input
    }
    my_bag = 'shiny gold'

    s1 = count_container(bags, my_bag)
    s2 = count_contained(bags, my_bag)

    print(s1)
    print(s2)


main()
