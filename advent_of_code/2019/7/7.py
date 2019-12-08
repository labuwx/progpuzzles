#!/usr/bin/env python3

import operator
import itertools as it
from collections import deque


def run(mem, inl):
    mem = list(mem)
    pos = 0
    while True:
        pm, opc = mem[pos] // 100, mem[pos] % 100
        if opc == 1:  # add
            op = operator.add
            il, ol = 2, 1
        elif opc == 2:  # mul
            op = operator.mul
            il, ol = 2, 1
        elif opc == 3:  # read
            op = inl.popleft
            il, ol = 0, 1
        elif opc == 4:  # print
            op = lambda x: x
            il, ol = 1, 0
        elif opc == 5:  # jump-if-true
            op = lambda c, v: v if c else None
            il, ol = 2, 2
        elif opc == 6:  # jump-if-false
            op = lambda c, v: v if not c else None
            il, ol = 2, 2
        elif opc == 7:  # less than
            op = lambda x, y: int(x < y)
            il, ol = 2, 1
        elif opc == 8:  # equals
            op = lambda x, y: int(x == y)
            il, ol = 2, 1
        elif opc == 99:  # halt
            break
        else:
            print('Wrong opc %d at %d' % (opc, pos))
            print(list(enumerate(mem)))
            exit()

        inp = []
        for _ in range(il):
            v = mem[(pos := pos + 1)]
            inp.append(v if pm % 10 else mem[v])
            pm //= 10

        ret = op(*inp)
        if ol == 1:
            mem[mem[(pos := pos + 1)]] = ret
        pos += 1

        if ol == 2 and ret != None:
            pos = ret

        if opc == 4:
            yield ret


def measure(mem, perm):
    inps = [deque([phase]) for phase in perm]
    machines = [run(mem, iq) for iq in inps]
    i = 0
    for m, iq in it.cycle(zip(machines, inps)):
        iq.append(i)
        if (itmp := next(m, None)) != None:
            i = itmp
        else:
            break
    return i


def main():
    input = open('input').read()
    mem = [int(x) for x in input.split(',')]

    s1 = max(measure(mem, perm) for perm in it.permutations(range(5)))
    s2 = max(measure(mem, perm) for perm in it.permutations(range(5, 10)))

    print(s1)
    print(s2)


main()
