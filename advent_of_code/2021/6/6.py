#!/usr/bin/env python3


from collections import Counter, deque


def simul(initpop, n):
    population = deque(initpop)
    for _ in range(n):
        population.rotate(-1)
        population[-3] += population[-1]
    return sum(population)


def main():
    input = open('input').read().strip()
    input = [int(x) for x in input.split(',')]

    c = Counter(input)
    population = [c[i] for i in range(9)]

    s1 = simul(population, 80)
    s2 = simul(population, 256)

    print(s1)
    print(s2)


main()
