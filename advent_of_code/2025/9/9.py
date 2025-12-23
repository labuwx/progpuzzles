#!/usr/bin/env python3


import itertools as it


def area(x1, y1, x2, y2):
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


def main():
    input = open('input').read()
    # input = open('input_test').read()

    input = [tuple(int(x) for x in l.split(',')) for l in input.strip().splitlines()]
    lines = list(zip(input, input[1:] + input[:1]))

    s1 = s2 = 0
    for (x1, y1), (x2, y2) in it.combinations(input, 2):
        a = area(x1, y1, x2, y2)
        s1 = max(s1, a)

        if a <= s2:
            continue

        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        cx, cy = x1 + x2, y1 + y2

        r = 0
        for (lx1, ly1), (lx2, ly2) in lines:
            lx1, lx2 = sorted([lx1, lx2])
            ly1, ly2 = sorted([ly1, ly2])

            # check that the curve has no point inside the rectangle => the rectangle is either full or empty
            if (x1 < lx1 == lx2 < x2 and y1 < ly2 and ly1 < y2) or (
                y1 < ly1 == ly2 < y2 and x1 < lx2 and lx1 < x2
            ):
                break

            # ray casting: y = cy, x = cx -> +inf
            r += (cx <= 2 * lx1 == 2 * lx2 and 2 * ly1 <= cy <= 2 * ly2) or (
                cy == 2 * ly1 == 2 * ly2 and cx <= 2 * ly2
            )
        else:
            if r % 2:  # make sure the rectangle is not empty
                s2 = a

    print(s1)
    print(s2)


main()
