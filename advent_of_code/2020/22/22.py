#!/usr/bin/env python3

from collections import deque


def score(deck):
    score = 0
    for i, card in enumerate(reversed(deck)):
        score += (i + 1) * card
    return score


def play1(decks):
    decks = [deque(deck) for deck in decks]

    while all(decks):
        cards = [deck.popleft() for deck in decks]
        winner = int(cards[0] < cards[1])
        decks[winner].extend(sorted(cards, reverse=True))

    return score(decks[winner])


def play2(decks):
    def play2_inner(decks):
        decks = [deque(deck) for deck in decks]

        seen = set()
        while all(decks):
            state = tuple(tuple(deck) for deck in decks)
            if state in seen:
                winner = 0
                break
            else:
                seen.add(state)

            cards = [deck.popleft() for deck in decks]

            if all(len(deck) >= card for deck, card in zip(decks, cards)):
                next_decks = [list(deck)[:card] for deck, card in zip(decks, cards)]
                winner = play2_inner(next_decks)[0]
            else:
                winner = int(cards[0] < cards[1])
            decks[winner].extend([cards[winner], cards[(winner + 1) % 2]])

        return winner, decks[winner]

    return score(play2_inner(decks)[1])


def main():
    input = open('input').read().strip().split('\n\n')
    cards = [[int(l) for l in ctxt.split('\n')[1:]] for ctxt in input]

    s1 = play1(cards)
    s2 = play2(cards)

    print(s1)
    print(s2)


main()
