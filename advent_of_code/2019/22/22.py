#!/usr/bin/env python3

import re
from collections import deque
from sympy import mod_inverse


def shuffle(moves, cards):
    n, cards = len(cards), deque(cards)
    for move, k in moves:
        if move == 0:
            cards.reverse()
        elif move == 1:
            cards.rotate(-k)
        else:
            # assert gcd(n, k) == 1
            new_deck = deque([None]) * n
            while cards:
                new_deck[0] = cards.popleft()
                new_deck.rotate(-k)
            cards = new_deck
    assert None not in cards
    return cards


def rev_compile(moves, n, niter=1):
    a, b = 1, 0
    for move, k in reversed(moves):
        if move == 0:
            a, b = (-a) % n, (n - 1 - b) % n
        elif move == 1:
            a, b = a % n, (b + k) % n
        else:
            # assert gcd(n, k) == 1
            k_inv = mod_inverse(k, n)
            a, b = (k_inv * a) % n, (k_inv * b) % n

    aa = pow(a, niter, n)
    bb = (b * (1 - aa) * mod_inverse((1 - a), n)) % n
    f = lambda p: (aa * p + bb) % n

    return f


def main():
    input = [l.strip() for l in open('input').read().strip().split('\n')]
    rx = re.compile(
        r'^(?P<type>cut|deal with increment|deal into new stack)\s*(?P<n>-?\d+)?'
    )
    techmap = {'deal into new stack': 0, 'cut': 1, 'deal with increment': 2}
    moves = [
        (techmap[m.group('type')], int(n) if (n := m.group('n')) != None else None)
        for m in (rx.match(l) for l in input)
    ]

    cards1 = shuffle(moves, range(10007))
    s1 = cards1.index(2019)

    f = rev_compile(moves, 119315717514047, 101741582076661)
    s2 = f(2020)

    print(s1)
    print(s2)


main()
