#!/usr/bin/env python3

import itertools as it


def inc_pwd(pwd):
    pwd = list(reversed(pwd))

    for i in range(len(pwd)):
        c = pwd[i]
        if c == 'z':
            pwd[i] = 'a'
        else:
            pwd[i] = chr(ord(c) + 1)
            break
    else:
        pwd.append('a')

    pwd = ''.join(reversed(pwd))
    return pwd


def check_pwd(pwd):
    crit1 = False
    for c1, c2, c3 in zip(pwd, pwd[1:], pwd[2:]):
        crit1 = crit1 or (ord(c1) + 1 == ord(c2) == ord(c3) - 1)

    crit2 = (set(pwd) & set('iol')) == set()

    crit3 = False
    for i in range(len(pwd) - 3):
        if pwd[i] != pwd[i + 1]:
            continue
        for j in range(i + 2, len(pwd) - 1):
            crit3 = crit3 or (pwd[j] == pwd[j + 1] and pwd[i] != pwd[j])

    return crit1 and crit2 and crit3


def pwd_gen(pwd=''):
    while True:
        pwd = inc_pwd(pwd)
        if check_pwd(pwd):
            yield pwd


def main():
    input = open('input').read().strip().lower()

    santa_gen = pwd_gen(input)
    s1, s2 = it.islice(santa_gen, 2)

    print(s1)
    print(s2)


main()
