#!/usr/bin/env python3


def hash(s):
    v = 0
    for c in s:
        v = (17 * (v + ord(c))) % 256
    return v


def parse_cmd(s):
    if s[-1] == '-':
        return (s[:-1], None)
    else:
        a, b = s.split('=')
        return (a, int(b))


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = input.strip().split(',')

    s1, M = 0, [[] for _ in range(256)]
    for s in input:
        s1 += hash(s)

        r, v = parse_cmd(s)
        m = M[hash(r)]
        i = next((i for i, cmd in enumerate(m) if cmd[0] == r), None)

        match (i, v):
            case (None, None):
                pass
            case (None, _):
                m.append((r, v))
            case (_, None):
                del m[i]
            case (_, _):
                m[i] = (r, v)

    s2 = 0
    for k, m in enumerate(M):
        for j, (r, v) in enumerate(m):
            s2 += (1 + k) * (1 + j) * v

    print(s1)
    print(s2)


main()
