#!/usr/bin/env python3

from collections import deque
import re


rx = r'''Register A: (?P<RA>\d+)
Register B: (?P<RB>\d+)
Register C: (?P<RC>\d+)

Program: (?P<P>[0-7](,[0-7])*)'''

RA, RB, RC = 0, 1, 2


def run(program, regs):
    regs = list(regs)
    ip = 0
    while ip in range(len(program)):
        intsr = program[ip]
        v = program[ip + 1]

        # combo
        if 0 <= v <= 3:
            cv = v
        elif 4 <= v <= 6:
            cv = regs[v - 4]
        else:
            cv = None

        ip += 2
        out = None
        match intsr:
            case 0:  # adv
                regs[RA] = regs[RA] >> cv
            case 1:  # bxl
                regs[RB] ^= v
            case 2:  # bst
                regs[RB] = cv % 8
            case 3:  # jnz
                if regs[RA]:
                    ip = v
            case 4:  # bxc
                regs[RB] ^= regs[RC]
            case 5:  # out
                out = cv % 8
            case 6:  # bdv
                regs[RB] = regs[RA] >> cv
            case 7:  # cdv
                regs[RC] = regs[RA] >> cv

        yield out


def main():
    input = open('input').read()
    # input = open('input_test_1').read()
    # input = open('input_test_2').read()

    m = re.fullmatch(rx, input.strip())
    regs = [int(m['RA']), int(m['RB']), int(m['RC'])]
    program = [int(x) for x in m['P'].split(',')]

    s1 = ','.join(str(x) for x in run(program, regs) if x is not None)
    print(s1)

    q = deque()
    k, s2 = 0, None
    lp = len(program)
    while s2 is None:
        regs[RA] = k
        q.append((k, 0, run(program, regs)))

        for _ in range(len(q)):
            kk, l, runp = q.popleft()

            x = next(runp, (None,))

            if x == (None,) and l == lp:
                # assumes there is no smaller kk
                s2 = kk
            elif x == None:
                q.append((kk, l, runp))
            elif l < lp and x == program[l]:
                q.append((kk, l + 1, runp))

        k += 1

    print(s2)


main()
