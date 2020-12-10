#!/usr/bin/env python3

import itertools as it
import math
import pandas as pd
import re


boss_pattern = re.compile(
    r'Hit Points: (?P<hp>\d+)\nDamage: (?P<dmg>\d+)\nArmor: (?P<armor>\d+)'
)


def play(boss, player):
    lives_boss = math.ceil(boss['hp'] / max(1, player['dmg'] - boss['armor']))
    lives_player = math.ceil(player['hp'] / max(1, boss['dmg'] - player['armor']))
    return lives_player >= lives_boss


def main():
    shop = pd.read_csv('shop.csv', sep=' ')
    input = open('input').read().strip()
    boss = {
        p: int(m[p]) for m in [boss_pattern.search(input)] for p in ['hp', 'dmg', 'armor']
    }
    hp0 = 100

    mod_shop = shop.append(
        [
            {'name': 'NOARMOR', 'type': 'armor', 'cost': 0, 'dmg': 0, 'armor': 0},
            {'name': 'NORING1', 'type': 'ring', 'cost': 0, 'dmg': 0, 'armor': 0},
            {'name': 'NORING2', 'type': 'ring', 'cost': 0, 'dmg': 0, 'armor': 0},
        ],
        ignore_index=True,
    )

    cost_min, cost_max = math.inf, -1
#fmt: off
    for wp_cost, wp_dmg in mod_shop[mod_shop['type'] == 'weapon'][['cost', 'dmg']].itertuples(index=False):
        for arm_cost, arm_armor in mod_shop[mod_shop['type'] == 'armor'][['cost', 'armor']].itertuples(index=False):
            for (r1_cost, r1_dmg, r1_armor), (r2_cost, r2_dmg, r2_armor) in it.product(
                mod_shop[mod_shop['type'] == 'ring'][['cost', 'dmg', 'armor']].itertuples(index=False),
                repeat=2,
            ):
#fmt: on
                player = {
                    'hp': hp0,
                    'dmg': wp_dmg + r1_dmg + r2_dmg,
                    'armor': arm_armor + r1_armor + r2_armor,
                }

                if play(boss, player):
                    cost = wp_cost + arm_cost + r1_cost + r2_cost
                    cost_min = min(cost_min, cost)
                else:
                    cost = wp_cost + arm_cost + r1_cost + r2_cost
                    cost_max = max(cost_max, cost)

    print(cost_min)
    print(cost_max)


main()
