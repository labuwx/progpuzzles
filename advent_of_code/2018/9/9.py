#!/usr/bin/env python3

import re
from collections import deque


def win_score(nump, numm):
    player, q = 0, deque([0])
    scores = [0] * nump
    for point in range(1, numm + 1):
        if point % 23:
            q.rotate(-1)
            q.append(point)
        else:
            q.rotate(7)
            scores[player] += point + q.pop()
            q.rotate(-1)

        player = (player + 1) % nump
    return max(scores)


input = open('input').read().strip()
m = re.match(r'^(?P<players>\d+) players; last marble is worth (?P<marbles>\d+) points', input)
nump, numm = int(m.group('players')), int(m.group('marbles'))

# nump, numm = 9, 25
# nump, numm = 10, 1618
# nump, numm = 13, 7999

s1 = win_score(nump, numm)
s2 = win_score(nump, numm * 100)

print(s1)
print(s2)
