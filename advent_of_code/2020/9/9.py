#!/usr/bin/env python3

from collections import Counter, defaultdict
import itertools as it


def main():
    input = [int(x) for x in open('input').read().split()]
    len_preamb = 25

    prevn = Counter(input[:len_preamb])
    for i, n in it.islice(enumerate(input), len_preamb, None):
        fnd = False
        for k in prevn:
            kk = n - k
            if kk in prevn and (k != kk or prevn[k] > 1):
                fnd = True
                break
        if not fnd:
            s1 = n
            break
        prevn[n] += 1
        item_to_del = input[i - len_preamb]
        prevn[item_to_del] -= 1
        if prevn[item_to_del] == 0:
            del prevn[item_to_del]

    sn = 0
    integral_msg = defaultdict(list)
    for i, n in enumerate(input):
        sn += n
        integral_msg[sn].append((i, n))

    for sx, li in integral_msg.items():
        for ix, x in li:
            sy = sx - x + s1
            if sy in integral_msg:
                iy = next((iy for iy, y in integral_msg[sy] if iy > ix), None)
                if iy != None:
                    s2 = min(input[ix : iy + 1]) + max(input[ix : iy + 1])
                    break

    print(s1)
    print(s2)


main()
