#!/usr/bin/env python3


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = [tuple(int(y) for y in x.split('-')) for x in input.strip().split(',')]

    s1 = s2 = 0
    for x, y in input:
        for z in range(x, y + 1):
            zs = f'{z}'
            b1 = b2 = False
            for k in range(1, len(zs) // 2 + 1):
                if len(zs) % k:
                    continue

                b = all(zs[i] == zs[i - k] for i in range(k, len(zs)))
                b1 |= b and 2 * k == len(zs)
                b2 |= b

            s1 += z * b1
            s2 += z * b2

    print(s1)
    print(s2)


main()
