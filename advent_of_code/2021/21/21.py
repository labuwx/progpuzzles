#!/usr/bin/env python3

from collections import Counter
from heapq import heappush, heappop
import itertools as it


def parse_input(input):
    poss = tuple(int(l.split()[-1]) for l in input.split('\n'))

    return poss


def det_die():
    k = 0
    while True:
        k = k % 100 + 1
        yield k


# could be calculated, without simulation
def play1(pos, die):
    pos = list(pos)
    scores = [0, 0]
    curr_player = 0
    for i in it.count(1):
        other_player = (curr_player + 1) % 2
        steps = sum(next(die) for _ in range(3))
        pos[curr_player] = (pos[curr_player] + steps - 1) % 10 + 1
        scores[curr_player] += pos[curr_player]

        if scores[curr_player] >= 1000:
            return 3 * i * scores[other_player]

        curr_player = other_player


dirac_die = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


def play2(start_pos):
    # (scores, pos, curr_player)
    # scores always increases (tuple cmp) with a die throw, so good for heap cmp
    init_state = ((0, 0), tuple(start_pos), 0)
    q = [init_state]
    n_reached = Counter({init_state: 1})
    win_cnt = [0, 0]
    while q:
        state = heappop(q)
        scores, pos, curr_player = state
        nm = n_reached.pop(state)

        for throw, nnm in dirac_die.items():
            next_scores, next_pos = list(scores), list(pos)
            next_pos[curr_player] = (pos[curr_player] + throw - 1) % 10 + 1
            next_scores[curr_player] += next_pos[curr_player]

            if next_scores[curr_player] >= 21:
                win_cnt[curr_player] += nm * nnm
                continue

            next_state = (tuple(next_scores), tuple(next_pos), (curr_player + 1) % 2)
            if next_state not in n_reached:
                heappush(q, next_state)

            n_reached[next_state] += nm * nnm

    return win_cnt


def main():
    input = open('input').read().strip()
    # input = open('input_test').read().strip()

    start_pos = parse_input(input)

    s1 = play1(start_pos, det_die())
    s2 = max(play2(start_pos))

    print(s1)
    print(s2)


main()
