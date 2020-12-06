#!/usr/bin/env python3


def main():
    input = open('input').read().strip()
    answers = [
        [set(answer) for answer in group.split()] for group in input.split('\n\n')
    ]

    s1 = sum(len(set.union(*group)) for group in answers)
    s2 = sum(len(set.intersection(*group)) for group in answers)

    print(s1)
    print(s2)


main()
