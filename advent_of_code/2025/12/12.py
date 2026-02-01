#!/usr/bin/env python3


def main():
    input = open('input').read()
    # input = open('input_test').read()

    input = input.strip().split('\n\n')

    shapes = [
        {
            (x, y)
            for y, l in enumerate(shape.splitlines()[1:])
            for x, c in enumerate(l)
            if c == '#'
        }
        for shape in input[:-1]
    ]

    trees = []
    for l in input[-1].splitlines():
        area, *presents = l.split()
        area = tuple(int(x) for x in area[:-1].split('x'))
        presents = [int(x) for x in presents]
        trees.append((area, presents))

    # this should not work
    s1 = 0
    for t in trees:
        area = t[0][0] * t[0][1]
        for s, k in zip(shapes, t[-1]):
            area -= len(s) * k
        s1 += area >= 0

    print(s1)


main()
