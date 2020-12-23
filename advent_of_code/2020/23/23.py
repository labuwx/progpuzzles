#!/usr/bin/env python3

import itertools as it


def arr_to_deq(l):
    deq = [None] * (len(l) + 1)
    for i, j, k in zip(l, it.islice(l, 1, None), it.islice(l, 2, None)):
        deq[j] = [i, k]
    deq[l[0]] = [l[-1], l[1]]
    deq[l[-1]] = [l[-2], l[0]]
    return deq


def take(deq, head, n):
    l = []
    for _ in range(n):
        head = deq[head][1]
        l.append(head)
    return l


def deq_to_arr(deq, head):
    return take(deq, head, len(deq) - 1)


def move(deq, idx_from, idx_to, n):
    e_start = deq[idx_from][1]
    e_end = e_start
    for _ in range(n - 1):
        e_end = deq[e_end][1]

    deq[idx_from][1] = deq[e_end][1]
    deq[deq[e_end][1]][0] = idx_from

    deq[e_end][1] = deq[idx_to][1]
    deq[deq[e_end][1]][0] = e_end

    deq[idx_to][1] = e_start
    deq[e_start][0] = idx_to


def step(cups, curr_cup, nstep=1):
    cups = list(cups)
    cmax = len(cups) - 1

    for i in range(nstep):
        mv_cups = take(cups, curr_cup, 3)
        next_cup = next(
            k
            for k in it.chain(range(curr_cup - 1, 0, -1), range(cmax, curr_cup, -1))
            if k not in mv_cups
        )

        move(cups, curr_cup, next_cup, 3)
        curr_cup = cups[curr_cup][1]

    return cups, curr_cup


def labels(cups):
    l = deq_to_arr(cups, 1)
    s = ''.join(str(x) for x in l[:-1])
    return s


def main():
    input = [int(x) for x in open('input').read().strip()]

    cups1 = arr_to_deq(input)
    s1 = labels(step(cups1, input[0], 100)[0])

    cups2 = arr_to_deq(input + list(range(max(input) + 1, 1000000 + 1)))
    r = take(step(cups2, input[0], 10000000)[0], 1, 2)
    s2 = r[0] * r[1]

    print(s1)
    print(s2)


main()
