#!/usr/bin/env python3

import itertools as it
import math


def parse_input(input):
    dirs, netws = input.strip().split('\n\n')
    dirs = dirs.strip()

    network = {l[0:3]: (l[7:10], l[12:15]) for l in netws.split('\n')}

    return dirs, network


def simul(network, dirs, snode, enode):
    loc = snode
    for i, d in enumerate(it.cycle(dirs)):
        if loc == enode:
            return i

        dn = 0 if d == 'L' else 1
        loc = network[loc][dn]


# many assumptions here about the input
def find_cycle(network, dirs, snode):
    loc = snode
    zi = None
    for i, d in enumerate(it.cycle(dirs)):
        if loc[-1] == 'Z':
            if zi is None:
                zi = i
            else:
                assert i == 2 * zi
                return zi

        dn = 0 if d == 'L' else 1
        loc = network[loc][dn]


def main():
    input = open('input').read()
    # input = open('input_test_2').read()
    dirs, network = parse_input(input)

    s1 = simul(network, dirs, 'AAA', 'ZZZ')

    s2 = math.lcm(
        *(find_cycle(network, dirs, loc) for loc in network.keys() if loc[-1] == 'A')
    )

    print(s1)
    print(s2)


main()
