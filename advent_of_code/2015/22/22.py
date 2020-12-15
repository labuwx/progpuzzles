#!/usr/bin/env python3

import heapq
import itertools as it
import re


boss_pattern = re.compile(r'Hit Points: (?P<hp>\d+)\nDamage: (?P<dmg>\d+)')


spells = {
    'Magic Missile': {'cost': 53, 'time': 0, 'dmg': 4},
    'Drain': {'cost': 73, 'time': 0, 'dmg': 2, 'hp': 2},
    'Shield': {'cost': 113, 'time': 6, 'armor': 7},
    'Poison': {'cost': 173, 'time': 6, 'dmg': 3},
    'Recharge': {'cost': 229, 'time': 5, 'mana': 101},
}


def state(v):
    _, _, turn, (hp, mana), boss_hp, active_spells = v
    return (turn % 2, hp, mana, boss_hp, tuple(sorted(active_spells.items())))


def play(hp0, mana0, boss, dhard=False):
    rnd = it.count()
    # mana spent, rnd, turn, (hp, mana), boss hp, {(speel name, time remaining)}
    v = (0, next(rnd), 0, (hp0, mana0), boss['hp'], {})
    to_visit = [v]
    seen = {state(v)}
    while to_visit:
        d, _, turn, (hp, mana), boss_hp, active_spells = heapq.heappop(to_visit)

        armor = 0
        rem_spells = {}
        for spname, trem in active_spells.items():
            if trem > 1:
                rem_spells[spname] = trem - 1
            spell = spells[spname]

            if 'dmg' in spell:
                boss_hp -= spell['dmg']
            if 'mana' in spell:
                mana += spell['mana']
            if 'hp' in spell:
                hp += spell['hp']
            if 'armor' in spell:
                armor += spell['armor']

        if boss_hp <= 0:
            return d

        if turn % 2 == 1:
            hp -= max(1, boss['dmg'] - armor)
            if hp > 0:
                v = (d, next(rnd), turn + 1, (hp, mana), boss_hp, rem_spells)
                sv = state(v)
                if sv not in seen:
                    seen.add(sv)
                    heapq.heappush(to_visit, v)
        else:
            hp -= dhard
            if hp <= 0:
                continue
            for spname in spells.keys() - rem_spells.keys():
                spell = spells[spname]
                if spell['cost'] > mana:
                    continue
                cp_rem_spells = dict(rem_spells)
                cp_rem_spells[spname] = spell['time']
                v = (
                    d + spell['cost'],
                    next(rnd),
                    turn + 1,
                    (hp, mana - spell['cost']),
                    boss_hp,
                    cp_rem_spells,
                )
                sv = state(v)
                if sv not in seen:
                    seen.add(sv)
                    heapq.heappush(to_visit, v)


def main():
    input = open('input').read().strip()
    boss = {p: int(m[p]) for m in [boss_pattern.search(input)] for p in ['hp', 'dmg']}
    hp0, mana0 = 50, 500

    s1 = play(hp0, mana0, boss, dhard=False)
    s2 = play(hp0, mana0, boss, dhard=True)

    print(s1)
    print(s2)


main()
