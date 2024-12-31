#!/usr/bin/env python3

from collections import defaultdict, deque
import operator

AND, OR, XOR = operator.and_, operator.or_, operator.xor


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


# xi XOR yi      -> ai
# xi AND yi      -> bi
# ai XOR c_(i-1) -> zi
# ai AND c_(i-1) -> di
# di AND bi      -> ci
def fixadd(gates):
    X = lambda k: f'x{k:02}'
    Y = lambda k: f'y{k:02}'
    Z = lambda k: f'z{k:02}'
    idx = lambda gs: int(gs[1:])

    gates = [[frozenset(g[:2]), g[2], g[-1]] for g in gates]
    wires = {g[-1]: g for g in gates}
    ins = {tuple(g[:2]): g for g in gates}
    imax = max(idx(w) for g in gates if (w := g[-1]).startswith('z'))

    swaps = set()

    def assertfix(g1, w):
        nonlocal swaps
        if g1[-1] == w:
            return

        g2 = wires[w]
        w1, w2 = g1[-1], g2[-1]
        g1[-1], g2[-1] = w2, w1
        wires[w1], wires[w2] = g2, g1
        swaps |= {w1, w2}

    gz0 = ins[(frozenset({X(0), Y(0)}), XOR)]
    if gz0[-1] != Z(0):
        doswap(gz0, wires[Z(0)])

    gcarry = ins[(frozenset({X(0), Y(0)}), AND)]
    for i in range(1, imax):
        wcarry = gcarry[-1]

        gai = ins[(frozenset({X(i), Y(i)}), XOR)]
        gbi = ins[(frozenset({X(i), Y(i)}), AND)]

        gzi = next(g for g in gates if wcarry in g[0] and g[1] == XOR)
        assertfix(gzi, Z(i))

        wai = next(iter(gzi[0] - {wcarry}))
        assertfix(gai, wai)

        wdi = ins[(frozenset({wai, wcarry}), AND)][-1]
        gcarry = next((g for g in gates if wdi in g[0]), None)

        wbi = next(iter(gcarry[0] - {wdi}))
        assertfix(gbi, wbi)

    return sorted(swaps)


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
        op = {'AND': AND, 'OR': OR, 'XOR': XOR}[op]
        gates.append((v1, v2, op, v3))

    s1 = var2num(eval(vars, gates), 'z')
    s2 = ','.join(fixadd(gates))

    print(s1)
    print(s2)


main()
