#!/usr/bin/env python3

from collections import Counter


score_map = {')': (3, 1), ']': (57, 2), '}': (1197, 3), '>': (25137, 4)}
cpmap = {'(': ')', '[': ']', '{': '}', '<': '>'}
opmap = {c: o for o, c in cpmap.items()}


def check(l):
    stack = []
    for i, c in enumerate(l):
        if score := score_map.get(c):
            opair = opmap[c]
            if not (stack and stack.pop() == opair):
                return score[0], None
        else:
            stack.append(c)

    return 0, stack


def auto_comp_score(stack):
    score = 0
    for c in reversed(stack):
        score = 5 * score + score_map[cpmap[c]][1]
    return score


def mid(l):
    return sorted(l)[len(l) // 2]


def main():
    input = open('input').read().strip().split('\n')
    # input = open('input_test').read().strip().split('\n')

    s1, acomp_scores = 0, []
    for l in input:
        score, stack = check(l)
        if score > 0:
            s1 += score
        else:
            acomp_scores.append(auto_comp_score(stack))

    s2 = mid(acomp_scores)

    print(s1)
    print(s2)


main()
