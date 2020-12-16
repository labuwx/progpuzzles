#!/usr/bin/env python3

import itertools as it
import numpy as np


dirs = [(x, y) for x, y in it.product([-1, 0, 1], repeat=2) if not x == 0 == y]

# floor, empty, occupied
CF, CE, CO = '.', 'L', '#'


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def inrange(a, b, c):
    return all(ai <= bi < ci for ai, bi, ci in zip(a, b, c))


def neighbours(seats, pos, look_far):
    nbs = 0
    for d in dirs:
        npos = pos
        for _ in it.count() if look_far else range(1):
            npos = cadd(npos, d)
            if not inrange((0, 0), npos, seats.shape):
                break
            if seats[npos] == CO:
                nbs += 1
            if seats[npos] != CF:
                break

    return nbs


def arrange(seats, look_far=False, sticky_seat=False):
    change = True
    while change:
        new_seats = np.empty_like(seats)
        change = False
        for pos, x in np.ndenumerate(seats):
            if x == CF:
                v = CF
            else:
                nbs = neighbours(seats, pos, look_far)
                if (x == CO and nbs < 4 + sticky_seat) or (x == CE and nbs == 0):
                    v = CO
                else:
                    v = CE

            new_seats[pos] = v
            change = change or v != x

        seats = new_seats
    return seats


def main():
    input = open('input').read().split()
    shape = (len(input[0]), len(input))

    seats = np.fromfunction(np.vectorize(lambda x, y: input[y][x]), shape, dtype=object)

    seats1 = arrange(seats)
    s1 = np.sum(seats1 == CO)

    seats2 = arrange(seats, look_far=True, sticky_seat=True)
    s2 = np.sum(seats2 == CO)

    print(s1)
    print(s2)


main()
