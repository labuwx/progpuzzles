#!/usr/bin/env python3

from collections import deque


def main():
    input = open('input').read()
    # input = open('input_test').read()

    input = input.strip().split('\n\n')
    ranges = [tuple(int(x) for x in l.split('-')) for l in input[0].splitlines()]
    ingrs = deque(sorted(int(x) for x in input[1].splitlines()))
    q = deque(sorted((x, i) for r in ranges for i, x in enumerate(r)))

    s1 = s2 = 0
    k, y = 0, None
    while q:
        x = q[0][0]
        if y is None:
            y = x

        while ingrs and ingrs[0] < x:
            ingrs.popleft()
            s1 += k > 0

        while q and q[0][0] == x and q[0][1] == 0:
            q.popleft()
            k += 1

        while ingrs and ingrs[0] == x:
            ingrs.popleft()
            s1 += k > 0

        while q and q[0][0] == x and q[0][1] == 1:
            q.popleft()
            k -= 1

        if k == 0:
            s2 += x - y + 1
            y = None

    print(s1)
    print(s2)


main()
