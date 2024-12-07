#!/usr/bin/env python3


from collections import deque


def parse_input(txt):
    eqs = []
    for l in txt.strip().splitlines():
        xs = l.split()
        eqs.append((int(xs[0][:-1]), [int(x) for x in xs[1:]]))
    return eqs


def get_prefix(xy, y):
    xy_s, y_s = str(xy), str(y)
    if xy_s != y_s and xy_s.endswith(y_s):
        return int(xy_s[: -len(y_s)])
    else:
        return None


def test_eq(tv, xs, concat_op):
    q = deque([(tv, len(xs) - 1)])
    while q:
        v, i = q.popleft()
        x = xs[i]

        if i == 0:
            if v == x:
                return True
        else:
            if x <= v:
                q.append((v - x, i - 1))
            if v % x == 0:
                q.append((v // x, i - 1))
            if concat_op and (pref := get_prefix(v, x)) is not None:
                q.append((pref, i - 1))

    return False


def main():
    input = open('input').read()
    # input = open('input_test').read()

    eqs = parse_input(input)

    s1 = sum(tv for tv, xs in eqs if test_eq(tv, xs, concat_op=False))
    s2 = sum(tv for tv, xs in eqs if test_eq(tv, xs, concat_op=True))

    print(s1)
    print(s2)


main()
