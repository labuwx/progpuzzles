#!/usr/bin/env python3

from collections import defaultdict, deque
import operator


def eval(vars, gates):
    vars = dict(vars)

    q = deque()
    gatemap = defaultdict(list)
    for gate in gates:
        v1, v2 = gate[:2]
        gatemap[v1].append(gate)
        gatemap[v2].append(gate)
        if v1 in vars and v2 in vars:
            q.append(gate)

    while q:
        v1, v2, op, v3 = q.pop()
        vars[v3] = op(vars[v1], vars[v2])
        for gate in gatemap[v3]:
            if gate[0] in vars and gate[1] in vars:
                q.append(gate)

    return vars


def var2num(vars, prefix):
    return sum(
        val * 2 ** int(var[1:]) for var, val in vars.items() if var.startswith(prefix)
    )


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = input.strip().split('\n\n')

    vars = {
        var: int(val) for l in input[0].splitlines() for var, val in [l.split(': ')]
    }

    gates = []
    for l in input[1].splitlines():
        v1, op, v2, _, v3 = l.split(' ')
        op = {'AND': operator.and_, 'OR': operator.or_, 'XOR': operator.xor}[op]
        gates.append((v1, v2, op, v3))

    s1 = var2num(eval(vars, gates), 'z')

    print(s1)


main()
