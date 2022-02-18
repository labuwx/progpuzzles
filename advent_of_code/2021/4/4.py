#!/usr/bin/env python3

from collections import Counter


def unique(l):
    return len(l) == len(set(l))


def parse_board(bs):
    board = {}
    for y, l in enumerate(bs.split('\n')):
        for x, v in enumerate(l.split()):
            board[(x, y)] = int(v)

    # the "each board contains unique numbers" assertion is used throughout this code
    assert unique(board.values())

    return board


# this could be coroutine
def play(draw, board):
    # precompute for fast calculation
    subscore, revboard = 0, {}
    rowc, colc = Counter(), Counter()
    for p, x in board.items():
        subscore += x
        revboard[x] = p
        colc[p[0]] += 1
        rowc[p[1]] += 1

    for i, x in enumerate(draw):
        if (p := revboard.get(x)) is None:
            continue
        subscore -= x
        colc[p[0]] -= 1
        rowc[p[1]] -= 1
        if colc[p[0]] == 0 or rowc[p[1]] == 0:
            break
    else:
        assert False

    score = subscore * x
    return i, score


def main():
    input = open('input').read().strip().split('\n\n')
    # input = open('input_test').read().strip().split('\n\n')
    draw = [int(x) for x in input[0].split(',')]
    boards = [parse_board(b) for b in input[1:]]
    assert unique(draw)

    plays = [play(draw, board) for board in boards]

    s1 = min(plays, key=lambda p: p[0])[1]
    s2 = max(plays, key=lambda p: p[0])[1]

    print(s1)
    print(s2)


main()
