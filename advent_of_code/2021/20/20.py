#!/usr/bin/env python3

import itertools as it


conv_mask = [
    ((dx, dy), 2 ** (-dx - dy * 3 + 4)) for dx, dy in it.product([-1, 0, 1], repeat=2)
]


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def parse_input(input):
    algo, image = input.split('\n\n')
    algo = [c == '#' for c in algo]
    assert len(algo) == 512

    image = {
        (x, y)
        for y, l in enumerate(image.split('\n'))
        for x, c in enumerate(l)
        if c == '#'
    }

    return algo, (False, image)


def enhance(algo, image, n=1):
    background, foreground = image
    for _ in range(n):
        xm = min(x for x, _ in foreground)
        XM = max(x for x, _ in foreground)
        ym = min(y for _, y in foreground)
        YM = max(y for _, y in foreground)
        new_bg = algo[511 * background]
        new_fg = set()

        for coord in it.product(range(xm - 1, XM + 2), range(ym - 1, YM + 2)):
            index = sum(
                weight
                for dcoord, weight in conv_mask
                if (cadd(coord, dcoord) in foreground) != background
            )
            if algo[index] != new_bg:
                new_fg.add(coord)

        background = new_bg
        foreground = new_fg

    return background, foreground


def main():
    input = open('input').read().strip()
    # input = open('input_test').read().strip()

    algo, init_image = parse_input(input)

    s1 = len(enhance(algo, init_image, n=2)[1])
    s2 = len(enhance(algo, init_image, n=50)[1])

    print(s1)
    print(s2)


main()
