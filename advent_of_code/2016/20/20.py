#!/usr/bin/env python3


def main():
    input = open('input').read().strip().split('\n')
    blacklist = [
        (int(ls[0]), int(ls[1])) for l in input for ls in [l.strip().split('-')]
    ]
    addr_max = 2 ** 32 - 1

    blkl = sorted(blacklist) + [(addr_max + 1, addr_max + 1)]
    last_end = -1
    s1, s2 = None, 0
    for start, end in blkl:
        if start > last_end + 1:
            s1 = last_end + 1 if s1 == None else s1
            s2 += start - last_end - 1
        last_end = max(last_end, end)

    print(s1)
    print(s2)


main()
