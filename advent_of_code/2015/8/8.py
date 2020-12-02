#!/usr/bin/env python3


def parse(str_raw):
    assert str_raw[0] == str_raw[-1] == '"'

    str_par, i = '', 1
    while i < len(str_raw) - 1:
        c0 = str_raw[i]
        if c0 != '\\':
            str_par += c0
            i += 1
        else:
            c1 = str_raw[i + 1]
            if c1 in ('\\', '"'):
                str_par += c1
                i += 2
            elif c1 == 'x':
                str_par += chr(int(str_raw[i + 2 : i + 4], 16))
                i += 4
            else:
                assert false

    return str_par


def encode(str_raw):
    str_enc = '"'

    for c in str_raw:
        if c in ('\\', '"'):
            str_enc += '\\'
        str_enc += c

    str_enc += '"'

    return str_enc


def main():
    input = open('input').read().strip().split('\n')

    nraw, nparsed, nencoded = 0, 0, 0
    for l in input:
        nraw += len(l)
        str_par = parse(l)
        str_enc = encode(l)
        nparsed += len(str_par)
        nencoded += len(str_enc)

    s1 = nraw - nparsed
    s2 = nencoded - nraw

    print(s1)
    print(s2)


main()
