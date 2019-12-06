#!/usr/bin/env python3


def full_orbit(dorbits, p):
    forbit = [p]
    while forbit[-1] != 'COM':
        forbit.append(next(pi for pi, po in dorbits if po == forbit[-1]))
    return list(reversed(forbit))


def num_orb_trans(dorbits, p1, p2):
    f1 = full_orbit(dorbits, p1)
    f2 = full_orbit(dorbits, p2)
    k = next(i for i, (pp1, pp2) in enumerate(zip(f1, f2)) if pp1 != pp2)
    return len(f1) + len(f2) - 2 * k - 2


def sum_orbits(dorbits):
    norbits = {'COM': 0}
    change = True
    while change:
        change = False
        for pi, po in dorbits:
            if pi in norbits and po not in norbits:
                change = True
                norbits[po] = norbits[pi] + 1
    return sum(norbits.values())


def main():
    input = open('input').read().strip()
    dorbits = [tuple(l.split(')')) for l in input.split('\n')]

    s1 = sum_orbits(dorbits)
    s2 = num_orb_trans(dorbits, 'YOU', 'SAN')

    print(s1)
    print(s2)


main()
