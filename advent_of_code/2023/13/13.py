#!/usr/bin/env python3


def calcmirror(block, nsmudge=0):
    xM, yM = len(block[0]) - 1, len(block) - 1

    for x in range(xM):
        nsm = sum(
            block[y][x - k] != block[y][x + 1 + k]
            for k in range(min(x, xM - x - 1) + 1)
            for y in range(yM + 1)
        )
        if nsm == nsmudge:
            return x + 1

    for y in range(yM):
        nsm = sum(
            block[y - k][x] != block[y + k + 1][x]
            for k in range(min(y, yM - y - 1) + 1)
            for x in range(xM + 1)
        )
        if nsm == nsmudge:
            return (y + 1) * 100

    assert False


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = [block.splitlines() for block in input.strip().split('\n\n')]

    s1 = sum(calcmirror(b, nsmudge=0) for b in input)
    s2 = sum(calcmirror(b, nsmudge=1) for b in input)

    print(s1)
    print(s2)


main()
