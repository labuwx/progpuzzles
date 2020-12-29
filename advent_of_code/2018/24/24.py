#!/usr/bin/env python3

import copy
import regex as re


pattern = re.compile(
    r'(?P<units>\d+) units each with (?P<hp>\d+) hit points '
    r'(?:\((?:(?:(?:weak to (?:(?P<weak>\w+)(?:, )?)+)|(?:immune to (?:(?P<immune>\w+)(?:, )?)+))(?:; )?)+\) )?'
    r'with an attack that does (?P<dmg_size>\d+) (?P<dmg_type>\w+) damage at initiative (?P<init>\d+)'
)


def parse_unit(l):
    m = pattern.fullmatch(l)
    group = {
        'units': int(m['units']),
        'hp': int(m['hp']),
        'dmg_type': m['dmg_type'],
        'dmg_size': int(m['dmg_size']),
        'init': int(m['init']),
        'weakto': set(m.captures('weak')),
        'immuneto': set(m.captures('immune')),
    }
    return group


def eff_pow(g):
    return g['units'] * g['dmg_size']


def theo_dmg(g1, g2):
    if g1['dmg_type'] in g2['immuneto']:
        return 0
    elif g1['dmg_type'] in g2['weakto']:
        return 2
    else:
        return 1


def select(groups, selected, g):
    g = groups[g]
    target = max(
        (
            id
            for id, gt in groups.items()
            if gt['side'] != g['side']
            and g['dmg_type'] not in gt['immuneto']
            and id not in selected
        ),
        key=lambda id: (
            theo_dmg(g, groups[id]),
            eff_pow(groups[id]),
            groups[id]['init'],
        ),
        default=None,
    )
    if target is None:
        return None

    selected.add(target)
    return target


def simul(data):
    groups = dict(
        enumerate(group | {'side': side} for side, gs in data.items() for group in gs)
    )
    group_cnt = {side: len(gs) for side, gs in data.items()}

    change = True
    while all(group_cnt.values()) and change:
        change = False
        sel_order = sorted(
            groups, key=lambda g: (eff_pow(groups[g]), groups[g]['init']), reverse=True
        )
        selected = set()
        targets = sorted(
            [
                (g, target)
                for g in sel_order
                if (target := select(groups, selected, g)) != None
            ],
            key=lambda x: groups[x[0]]['init'],
            reverse=True,
        )

        for id, idt in targets:
            if id not in groups:
                continue
            g, gt = groups[id], groups[idt]
            dmg = eff_pow(g) * theo_dmg(g, gt)
            units_left = max(0, gt['units'] - dmg // gt['hp'])

            change = change or (units_left != gt['units'])

            if units_left == 0:
                group_cnt[gt['side']] -= 1
                del groups[idt]
            else:
                gt['units'] = units_left

    if not change:
        return None, None

    winner = next(g for g, c in group_cnt.items() if c > 0)
    rem_units = sum(g['units'] for g in groups.values())

    return winner, rem_units


def boost(data, b):
    data_boosted = copy.deepcopy(data)
    for group in data_boosted['Immune System']:
        group['dmg_size'] += b
    return data_boosted


def exp_search(f):
    n = 1
    while not f(n):
        n *= 2

    n_min, n_max = 0, n
    while n_min < n_max - 1:
        n = n_min + (n_max - n_min) // 2
        if f(n):
            n_max = n
        else:
            n_min = n

    return n_min if f(n_min) else n_max


def main():
    input = open('input').read().strip()
    data = {
        pl[0][:-1]: [parse_unit(l) for l in pl[1:]]
        for p in input.split('\n\n')
        for pl in [p.split('\n')]
    }

    s1 = simul(data)[1]

    min_boost = exp_search(lambda b: simul(boost(data, b))[0] == 'Immune System')
    s2 = simul(boost(data, min_boost))[1]

    print(s1)
    print(s2)


main()
