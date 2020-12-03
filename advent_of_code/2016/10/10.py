#!/usr/bin/env python3

from collections import defaultdict
import re


# note: for AoC generated inputs, the execution order is unambiguous
# assumption: execution order does not matter


pattern = re.compile(
    r'''^ (?:
          (?P<vinit> value\ (?P<val>\d+)\ goes\ to\ bot\ (?P<tobot>\d+)) |
          (?P<gives> bot\ (?P<frombot>\d+)\ gives\ low\ to\ (?P<lowtype> output | bot)\ (?P<lowto>\d+)\ and\ high\ to\ (?P<hightype> output | bot)\ (?P<highto>\d+))
        ) $''',
    flags=re.VERBOSE,
)


def main():
    input = open('input').read().strip().split('\n')

    prog_val, prog_gives = [], []
    for l in input:
        m = pattern.match(l)

        if m.group('vinit') != None:
            instr = (int(m.group('val')), int(m.group('tobot')))
            prog_val.append(instr)
        else:  # gives
            instr = (
                int(m.group('frombot')),
                (int(m.group('lowto')), m.group('lowtype')),
                (int(m.group('highto')), m.group('hightype')),
            )
            prog_gives.append(instr)

    pockets = defaultdict(set)
    for x, b in prog_val:
        pockets[b].add(x)

    output, change = defaultdict(set), True
    while change:
        change = False
        for frombot, (lowto, lowtype), (highto, hightype) in prog_gives:
            pocket = pockets[frombot]
            if len(pocket) < 2:
                continue
            assert len(pocket) == 2

            mi, ma = sorted(pocket)
            if (mi, ma) == (17, 61):
                s1 = frombot

            (pockets, output)[lowtype == 'output'][lowto].add(mi)
            (pockets, output)[hightype == 'output'][highto].add(ma)

            pockets[frombot] = set()
            change = True

    s2 = list(output[0])[0] * list(output[1])[0] * list(output[2])[0]

    print(s1)
    print(s2)


main()
