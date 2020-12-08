#!/usr/bin/env python3

# note: istrap = prev_left xor prev_right (xor is + in GF(2))


def gen_tile(adj):
    istrap = adj[0] != adj[2]
    return istrap


def adj_it(row):
    return zip([False] + row, row, row[1:] + [False])


def count_safe(row0, n_check):
    prev_row = list(row0)
    n_safe = row0.count(False)

    for _ in range(1, n_check):
        next_row = [gen_tile(adj) for adj in adj_it(prev_row)]
        n_safe += next_row.count(False)
        prev_row = next_row

    return n_safe


def main():
    input = open('input').read().strip()
    row0 = [True if c == '^' else False for c in input]
    n1, n2 = 40, 400000

    s1 = count_safe(row0, n1)
    s2 = count_safe(row0, n2)

    print(s1)
    print(s2)


main()
