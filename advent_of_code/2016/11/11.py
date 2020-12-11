#!/usr/bin/env python3

from collections import defaultdict, deque
import copy
import itertools as it
import re


pattern = re.compile(
    r'''(?:(?P<microchip>\w+)-compatible\ microchip) |
        (?:(?P<generator>\w+)\ generator)''',
    flags=re.VERBOSE,
)

# chip, generator
C, G = 0, 1


def frozendict(dct):
    return frozenset(dct.items())


def reached_top(lab, topfloor):
    return all(n == topfloor for n in lab[1].values())


def item_on_floor(lab, n):
    items = {t for t, k in lab[1].items() if k == n}
    return items


def check_comb(comb):
    gen_in_comb = any(item[1] == G for item in comb)
    if not gen_in_comb:
        return True

    return all((item, G) in comb for item, _ in comb)


def state(lab):
    elev, items = lab
    pairs = defaultdict(lambda: [None, None])
    for (item, tt), floor in items.items():
        pairs[item][tt] = floor
    items_key = tuple(sorted(tuple(p) for p in pairs.values()))

    return (elev, items_key)


def count_steps(lab0, topfloor):
    seen = {state(lab0)}
    q = deque([(lab0, 0)])
    while q:
        lab, d = q.popleft()
        if reached_top(lab, topfloor):
            return d

        elev = lab[0]
        items = item_on_floor(lab, elev)
        for jump in [-1, 1]:
            next_elev = elev + jump
            if not 0 <= next_elev <= topfloor:
                continue
            next_items = item_on_floor(lab, next_elev)

            for elev_comb in it.product(items, repeat=2):
                elev_comb = set(elev_comb)
                if not (
                    check_comb(elev_comb)
                    and check_comb(items - elev_comb)
                    and check_comb(next_items | elev_comb)
                ):
                    continue

                new_lab = copy.deepcopy(lab)
                new_lab[0] = next_elev
                for item in elev_comb:
                    new_lab[1][item] = next_elev
                fr_new_lab = state(new_lab)
                if fr_new_lab not in seen:
                    seen.add(fr_new_lab)
                    q.append((new_lab, d + 1))


def main():
    input = open('input').read().strip().split('\n')
    topfloor = len(input) - 1

    # elevator, items
    lab1 = [0, {}]
    for n, l in enumerate(input):
        for obj in pattern.findall(l):
            if obj[0] != '':
                lab1[1][(obj[0], C)] = n
            else:
                lab1[1][(obj[1], G)] = n

    s1 = count_steps(lab1, topfloor)

    lab2 = copy.deepcopy(lab1)
    lab2[1].update(
        {('elerium', C): 0, ('elerium', G): 0, ('dilithium', C): 0, ('dilithium', G): 0}
    )
    s2 = count_steps(lab2, topfloor)

    print(s1)
    print(s2)


main()
