#!/usr/bin/env python3

import numpy as np
from scipy.signal import convolve2d


def rule(x, n):
    return int((x and 2 <= n <= 3) or (not x and n == 3))


def stuck_corners(grid):
    w, h = grid.shape
    st_val = 1
    grid[(0, 0)] = st_val
    grid[(w - 1, 0)] = st_val
    grid[(0, h - 1)] = st_val
    grid[(w - 1, h - 1)] = st_val


def step(grid, nstep=1, *, stuck=False):
    if stuck:
        stuck_corners(grid)

    for _ in range(nstep):
        neighbours = convolve2d(grid, np.ones((3, 3), dtype=int), 'same') - grid
        grid = np.fromfunction(
            np.vectorize(lambda *pos: rule(grid[pos], neighbours[pos])),
            grid.shape,
            dtype=int,
        )
        if stuck:
            stuck_corners(grid)

    return grid


def main():
    input = open('input').read().split()
    shape = (len(input[0]), len(input))
    nstep = 100

    grid = np.fromfunction(
        np.vectorize(lambda x, y: 1 if input[y][x] == '#' else 0), shape, dtype=int
    )

    grid1 = step(grid, 100)
    s1 = np.sum(grid1)

    grid2 = step(grid, 100, stuck=True)
    s2 = np.sum(grid2)

    print(s1)
    print(s2)


main()
