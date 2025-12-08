#!/usr/bin/env python3


import itertools as it
from collections import Counter


class UF:
    def __init__(self, n):
        self._l = [[None, 0] for x in range(n)]

    def find(self, i):
        j = i
        while self._l[j][0] != None:
            j = self._l[j][0]

        while self._l[i][0] != None:
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


def main():
    n, input = 1000, open('input').read()
    # n, input = 10, open('input_test').read()

    input = [tuple(int(x) for x in l.split(',')) for l in input.strip().splitlines()]

    ds = sorted(
        (sum((xi - xj) ** 2 for xi, xj in zip(pi, pj)), i, j)
        for (i, pi), (j, pj) in it.combinations(enumerate(input), 2)
    )
    uf = UF(len(input))

    m = len(input)
    for k, (_, i, j) in enumerate(ds):
        if uf.find(i) != uf.find(j):
            uf.union(i, j)
            m -= 1

        if k + 1 == n:
            s1 = 1
            c = Counter(uf.find(ii) for ii, _ in enumerate(input))
            for _, r in c.most_common(3):
                s1 *= r

        if m == 1:
            s2 = input[i][0] * input[j][0]
            break

    print(s1)
    print(s2)


main()
