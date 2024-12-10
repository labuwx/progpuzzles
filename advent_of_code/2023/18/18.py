#!/usr/bin/env python3


dirmap = {'D': (0, -1), 'U': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
dirord = 'RDLU'


def parse_input(txt):
    digplan1, digplan2 = [], []
    for l in txt.strip().splitlines():
        d, k, c = l.split()
        hxd = c[2:-1]
        digplan1.append((dirmap[d], int(k)))
        digplan2.append((dirmap[dirord[int(hxd[-1])]], int(hxd[:-1], base=16)))

    return digplan1, digplan2


# see 2023/10 for more details
def find_volume(digplan):
    x, pdy = 0, None
    area, len_cyc = 0, 0
    for (dx, dy), k in digplan:
        len_cyc += k

        if pdy is not None:  # when pdy is unkown, x is 0 anyway
            area += x * (dy + pdy)

        area += 2 * x * dy * (k - 1)
        x += dx * k
        pdy = dy

    return abs(area) // 2 + len_cyc // 2 + 1


def main():
    input = open('input').read()
    # input = open('input_test').read()

    digplan1, digplan2 = parse_input(input)

    s1 = find_volume(digplan1)
    s2 = find_volume(digplan2)

    print(s1)
    print(s2)


main()
