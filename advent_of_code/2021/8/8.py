#!/usr/bin/env python3


# TODO: look for an even more general solution
# that uses every set operation (and not just the # of outcomes)
# check if per segment reversing is possible
# (it is possible for decimal digits)


def signature(collection, x):
    s = (
        len(x),  # size
        sum(x < y for y in collection),  # supersets
        sum(y < x for y in collection),  # subsets
    )
    return s


dig2seg = [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg',
]
dig2seg = {k: frozenset(v) for k, v in enumerate(dig2seg)}

seg_relation_to_dig = {
    signature(dig2seg.values(), disp): x for x, disp in dig2seg.items()
}
# hope that the signatures are unique
assert len(seg_relation_to_dig) == len(dig2seg)


def solve_permut(displays):
    map = {disp: seg_relation_to_dig[signature(displays, disp)] for disp in displays}
    return map


def parse_input(input):
    return [
        tuple([frozenset(d) for d in lp.split()] for lp in l.split('|')) for l in input
    ]


def main():
    input = open('input').read().strip().split('\n')
    # input = open('input_test_2').read().strip().split('\n')
    input = parse_input(input)

    unique_len = {len(dig2seg[d]): d for d in [1, 4, 7, 8]}
    s1 = sum((len(d) in unique_len) for l in input for d in l[1])

    s2 = 0
    for l in input:
        map = solve_permut(l[0])
        s2 += sum(map[disp] * 10**k for k, disp in enumerate(reversed(l[1])))

    print(s1)
    print(s2)


main()
