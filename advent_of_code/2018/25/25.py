#!/usr/bin/env python3

import itertools as it


class UF:
    def __init__(self, n):
        self._l = [[None, 0] for x in range(n)]

    def find(self, i):
        j = i
        while self._l[j][0] != None:
            j = self._l[j][0]

        while self._l[i][0] != None:
            # left side is tricky: https://docs.python.org/3/reference/expressions.html#evaluation-order
            # changing i and using it as an index at the same time
            self._l[i][0], i = j, self._l[i][0]

        return j

    def union(self, i, j):
        ir, jr = self.find(i), self.find(j)
        if ir == jr:
            return

        if self._l[ir][1] < self._l[jr][1]:
            ir, jr = jr, ir

        self._l[jr][0] = ir
        if self._l[ir][1] == self._l[jr][1]:
            self._l[ir][1] += 1


def manhattan(p1, p2):
    return sum(abs(c1 - c2) for c1, c2 in zip(p1, p2))


def main():
    input = open('input').read().strip().split('\n')
    data = [tuple((int(x) for x in l.split(','))) for l in input]

    uf = UF(len(data))
    for (i, p), (j, q) in it.combinations(enumerate(data), 2):
        if manhattan(p, q) <= 3:
            uf.union(i, j)

    clusters = {uf.find(i) for i, _ in enumerate(data)}
    s1 = len(clusters)

    print(s1)


main()
