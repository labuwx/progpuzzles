#!/usr/bin/env python3

from collections import deque, defaultdict


FFP, CONJ = '%', '&'
LP, HP = 0, 1


def parse_input(input):
    modules = {}
    for l in input.strip().splitlines():
        m, outs = l.split(' -> ')
        outs = outs.split(', ')

        if m[0] in [FFP, CONJ]:
            name = m[1:]
            type = m[0]
        else:
            name = m
            type = None

        modules[name] = (type, outs)

    return modules


def main():
    input = open('input').read()
    # input = open('input_test_1').read()
    # input = open('input_test_2').read()

    modules = parse_input(input)

    ffps = {name: LP for name, (t, _) in modules.items() if t == FFP}
    conjs = defaultdict(dict)
    for m, (_, outs) in modules.items():
        for out in outs:
            if out in modules and modules[out][0] == CONJ:
                conjs[out][m] = LP

    pulses = [0, 0]
    for _ in range(1000):
        q = deque([('broadcaster', LP, None)])
        while q:
            m, pulse, src = q.popleft()
            pulses[pulse] += 1

            if m not in modules:
                continue

            type, outs = modules[m]

            if type == FFP:
                if pulse == HP:
                    continue
                outp = ffps[m] = 1 - ffps[m]
            elif type == CONJ:
                conjs[m][src] = pulse
                outp = 1 - all(conjs[m].values())
            else:
                outp = pulse
            q.extend((out, outp, m) for out in outs)

    s1 = pulses[0] * pulses[1]
    print(s1)


main()
