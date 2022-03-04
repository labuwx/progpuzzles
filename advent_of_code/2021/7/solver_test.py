#!/usr/bin/env python3

from hypothesis import given, strategies as st

from solvers import *


@given(st.lists(st.integers(min_value=0, max_value=10000), min_size=1))
def solve1_1_2_eq(input):
    s1_1 = solve1_1(input)
    s1_2 = solve1_2(input)

    assert s1_1 == s1_2


@given(st.lists(st.integers(min_value=0, max_value=10000), min_size=1))
def solve1_2_4_eq(input):
    s1_2 = solve1_2(input)
    s1_4 = solve1_4(input)

    assert s1_2 == s1_4


@given(st.lists(st.integers(min_value=0, max_value=10000), min_size=1))
def solve1_3_4_eq(input):
    s1_3 = solve1_3(input)
    s1_4 = solve1_4(input)

    assert s1_3 == s1_4


@given(st.lists(st.integers(min_value=0, max_value=10000), min_size=1))
def solve1_4_5_eq(input):
    s1_4 = solve1_4(input)
    s1_5 = solve1_5(input)

    assert s1_4 == s1_5


@given(st.lists(st.integers(min_value=0, max_value=10000), min_size=1))
def solve2_1_2_eq(input):
    s2_1 = solve2_1(input)
    s2_2 = solve2_2(input)

    assert s2_1 == s2_2


@given(st.lists(st.integers(min_value=0, max_value=10000), min_size=1))
def solve2_2_3_eq(input):
    s2_2 = solve2_2(input)
    s2_3 = solve2_3(input)

    assert s2_2 == s2_3


def main():
    solve1_1_2_eq()
    solve1_2_4_eq()
    solve1_3_4_eq()
    solve1_4_5_eq()

    solve2_1_2_eq()
    solve2_2_3_eq()


main()
