#!/usr/bin/env python3


from collections import deque


def main():
    input = open('input').read()
    # input = open('input_test').read()

    M = []
    for l in input.strip().splitlines():
        ind, *btns, jolt = l.split()
        ind = tuple(c == '#' for c in ind[1:-1])
        btns = tuple(tuple(int(x) for x in btn[1:-1].split(',')) for btn in btns)
        jolt = tuple(int(x) for x in jolt[1:-1].split(','))
        M.append((ind, btns, jolt))

    s1 = 0
    for ind, btns, jolt in M:
        r = set()
        q = deque([(0, 0, tuple(False for _ in ind))])
        while True:
            k, i, ind_ = q.popleft()
            if ind_ == ind:
                s1 += k
                break

            if (key := (ind_, i)) in r:
                continue
            r.add(key)

            for j, btn in enumerate(btns[i:]):
                ind__ = list(ind_)
                for b in btn:
                    ind__[b] = not ind__[b]
                q.append((k + 1, i + j, tuple(ind__)))

    print(s1)
    # print(s2)


main()
