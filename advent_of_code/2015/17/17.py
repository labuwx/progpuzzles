#!/usr/bin/env python3

from collections import defaultdict


def main():
    input = open('input').read().split()
    containers = sorted(int(x) for x in input)
    amount = 150

    # tuple: comb, comb_min, used_min
    mem = defaultdict(lambda: (0, 0, 0), {(0, 0): (1, 1, 0)})
    for i, cap in enumerate(containers):
        for m in range(amount + 1):
            m_not_current = mem[(i, m)]
            m_use_current = mem[(i, m - cap)]

            if m_use_current[1] == 0 or (
                m_not_current[2] < m_use_current[2] + 1 and m_not_current[1] > 0
            ):
                comb_min = m_not_current[1]
                used_min = m_not_current[2]
            elif m_not_current[1] == 0 or (
                m_use_current[2] + 1 < m_not_current[2] and m_use_current[1] > 0
            ):
                comb_min = m_use_current[1]
                used_min = m_use_current[2] + 1
            else:
                comb_min = m_not_current[1] + m_use_current[1]
                used_min = m_not_current[2]

            mem[(i + 1, m)] = (
                m_not_current[0] + m_use_current[0],
                comb_min,
                used_min,
            )

    s1 = mem[(len(containers), amount)][0]
    s2 = mem[(len(containers), amount)][1]

    print(s1)
    print(s2)


main()
