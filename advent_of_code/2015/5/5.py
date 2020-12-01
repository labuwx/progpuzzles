#!/usr/bin/env python3


def isnice1(s):
    vowels = set('aeiou')
    crit1 = sum(c in vowels for c in s) >= 3

    crit2 = any(c1 == c2 for c1, c2 in zip(s, s[1:]))

    forb_subs = ['ab', 'cd', 'pq', 'xy']
    crit3 = all(subs not in s for subs in forb_subs)

    return crit1 and crit2 and crit3


def isnice2(s):
    crit1 = any(s[i : i + 2] in s[i + 2 :] for i in range(len(s) - 3))

    crit2 = any(c1 == c2 for c1, _, c2 in zip(s, s[1:], s[2:]))

    return crit1 and crit2


def main():
    input = open('input').read().split()

    s1 = sum(isnice1(s) for s in input)
    s2 = sum(isnice2(s) for s in input)

    print(s1)
    print(s2)


main()
