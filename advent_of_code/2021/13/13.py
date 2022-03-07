#!/usr/bin/env python3


def parse_input(input):
    dots, folds = input.split('\n\n')
    dots = {tuple(int(coord) for coord in l.split(',')) for l in dots.split('\n')}

    folds = [
        (x[0], int(x[1]))
        for l in folds.split('\n')
        for x in [l.split(' ')[-1].split('=')]
    ]

    return dots, folds


def print_dots(dots):
    x_max = max(x for x, _ in dots)
    y_max = max(y for _, y in dots)

    s = '\n'.join(
        ''.join('#' if (x, y) in dots else ' ' for x in range(x_max + 1))
        for y in range(y_max + 1)
    )

    return s


def main():
    input = open('input').read().strip()
    # input = open('input_test').read().strip()

    init_dots, folds = parse_input(input)

    dots = init_dots
    for i, (ax, v) in enumerate(folds):
        dots = {
            (
                v - abs(v - x) if ax == 'x' else x,
                v - abs(v - y) if ax == 'y' and True else y,
            )
            for x, y in dots
        }

        if i == 0:
            s1 = len(dots)

    s2 = print_dots(dots)

    print(s1)
    print(s2)


main()
