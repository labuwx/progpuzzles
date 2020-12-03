#!/usr/bin/env python3

import itertools as it


def rev_adj(s):
    return tuple(reversed(s))


def happyness_score(happyness_map, seating):
    score = sum(
        happyness_map[adj] + happyness_map[rev_adj(adj)]
        for adj in zip(seating, seating[1:])
    )
    missing_adj = (seating[0], seating[-1])
    score += happyness_map[missing_adj] + happyness_map[rev_adj(missing_adj)]
    return score


def main():
    input = open('input').read().strip().split('\n')
    mestring = 'MEME'

    happyness_map, guests = {}, set()
    for l in input:
        l = l.split()
        person = l[0]
        person_nt = l[-1][:-1]  # trim period from the end
        value = int(l[3]) * (1 if l[2] == 'gain' else -1)
        guests.update({person, person_nt})
        happyness_map[(person, person_nt)] = value
    for g in guests:
        happyness_map[(mestring, g)] = 0
        happyness_map[(g, mestring)] = 0
    guests = list(guests)

    s1 = max(
        happyness_score(happyness_map, (guests[0],) + seating)
        for seating in it.permutations(guests[1:])
    )
    s2 = max(
        happyness_score(happyness_map, (mestring,) + seating)
        for seating in it.permutations(guests)
    )

    print(s1)
    print(s2)


main()
