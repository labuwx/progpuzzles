#!/usr/bin/env python3

import math
import statistics


def linsum(d):
    return d * (d + 1) // 2


# brute force but how do we know that the solution is an integer?
# solution is int since inputs are int
# and the cost function is linear (or constant) between inputs
# cost function is linear combs of abs functions
# so takes extremal value on input elements (or at +-inf)
def solve1_1(input):
    s1 = math.inf
    for pos in range(min(input), max(input) + 1):
        cost = sum(abs(pos - pi) for pi in input)
        s1 = min(s1, cost)
    return s1


def solve1_2(input):
    input = sorted(input)
    cost = sum(input) - len(input) * input[0]
    s1, leftside = math.inf, 0
    for pos in range(input[0], input[-1] + 1):
        s1 = min(s1, cost)
        # diff eventually cahnges to >0, otherwise min would be in +inf
        # no need to compare after last iteration

        while leftside in range(len(input)) and input[leftside] == pos:
            leftside += 1
        diff = leftside - (len(input) - leftside)  # leftside - (rightside + onside)
        cost += diff
        # cost decreases until diff < 0
        #                      leftside < len(input) / 2
        # diff if constant between input elements
    return s1


# diff is constant between input elements
# so use only them as test positions
def solve1_3(input):
    input = sorted(input)
    cost = sum(input) - len(input) * input[0]
    prev = input[0]
    for leftside, pos in enumerate(input):
        if pos == prev:
            continue

        diff = 2 * leftside - len(input)
        if diff >= 0:
            break

        cost += diff * (pos - prev)
        prev = pos

    return cost


def solve1_4(input):
    input = sorted(input)
    opt_pos = input[len(input) // 2]
    cost = sum(abs(x - opt_pos) for x in input)
    return cost


def solve1_5(input):
    # int(median) is still a median since the inputs are integers
    opt_pos = int(statistics.median(input))
    cost = sum(abs(x - opt_pos) for x in input)
    return cost


def solve2_1(input):
    s2 = min(
        sum(linsum(abs(pos - pi)) for pi in input)
        for pos in range(min(input), max(input) + 1)
    )
    return s2


# bisect search
def solve2_2(input):
    cost = lambda pos: sum(linsum(abs(pos - pi)) for pi in input)
    m, M = min(input), max(input)
    while M - m > 1:
        mid = (m + M) // 2
        c_mid, c_right = cost(mid), cost(mid + 1)
        grad = c_right - c_mid

        if grad < 0:
            m = mid
        elif grad == 0:
            m = M = mid
        else:  # grad > 0
            M = mid

    # if m + 1 == M: m cannot have lower cost
    # for m to be the only optimum, it must have been a mid first
    # but then that mid would have had a >0 grad
    # so we would have moved M there, not m; -><-
    return cost(M)


# based on a paper by CrashAndSideburns:
# On the Unreasonable Efficacy of the Mean in Minimizing the Fuel Expenditure of Crab
# the continuous case optimum is within mean +- 1/2
# the discrete case optimum is within floor(m), ceil(M)
def solve2_3(input):
    mean = statistics.mean(input)
    m, M = math.floor(mean - 1 / 2), math.ceil(mean + 1 / 2)
    s2 = min(sum(linsum(abs(pos - pi)) for pi in input) for pos in range(m, M + 1))
    return s2
