#!/usr/bin/env python3

import copy
import regex as re

pattern = re.compile(r'(?:(?P<ing>\w+) ?)+(?:\(contains (?:(?P<all>\w+)(?:, )?)+\))?')


def find_bijection(map):
    map = copy.deepcopy(map)
    fixed, change = set(), True
    while change:
        change = False
        for k, v in map.items():
            if len(v) != 1 or k in fixed:
                continue
            fixed.add(k)
            v = next(iter(v))
            for k2, v2 in map.items():
                if k2 != k and v in v2:
                    change = True
                    v2.remove(v)
    map = {k: next(iter(v)) for k, v in map.items()}
    return map


def main():
    input = open('input_test').read().strip().split('\n')
    input = open('input').read().strip().split('\n')
    data = [
        (set(m.captures('ing')), set(m.captures('all')))
        for l in input
        for m in [pattern.match(l)]
    ]

    ingredients, allergens = set(), set()
    for ings, alls in data:
        ingredients.update(ings)
        allergens.update(alls)

    all_map = {all: set(ingredients) for all in allergens}
    for ings, alls in data:
        for all in alls:
            all_map[all] &= ings

    inert_ing = set(ingredients)
    for ings in all_map.values():
        inert_ing -= ings
    s1 = sum(len(ings & inert_ing) for ings, _ in data)

    dangerous_ingredients = [ing for _, ing in sorted(find_bijection(all_map).items())]
    s2 = ','.join(dangerous_ingredients)

    print(s1)
    print(s2)


main()
