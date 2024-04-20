#!/usr/bin/env python3


from collections import Counter

card_strength_1 = 'AKQJT98765432'
card_strength_1 = {c: i for i, c in enumerate(reversed(card_strength_1))}
card_strength_2 = dict(card_strength_1) | {'J': -1}


def parse_input(input):
    cards = []
    for l in input.split('\n'):
        hand, bid = l.split()
        cards.append((hand, int(bid)))
    return cards


def compkey(hand, joker=False):
    card_strength = card_strength_2 if joker else card_strength_1
    p2 = tuple(card_strength[c] for c in hand)

    handc = Counter(hand)
    if joker:
        jc = handc['J']
        handc['J'] = 0
        handc[handc.most_common(1)[0][0]] += jc
    handc = [x[1] for x in handc.most_common()]

    if handc[0] == 5:  # five of a kind
        p1 = 6
    elif handc[0] == 4:  # four of a kind
        p1 = 5
    elif handc[0] == 3 and handc[1] == 2:  # full house
        p1 = 4
    elif handc[0] == 3:  # three of a kind
        p1 = 3
    elif handc[0] == handc[1] == 2:  # two pair
        p1 = 2
    elif handc[0] == 2:  # one pair
        p1 = 1
    else:  # high card
        p1 = 0

    return (p1, p2)


def calc_win(cards, joker):
    cards_s = sorted(cards, key=lambda x: compkey(x[0], joker))
    acc = 0
    for i, (_, bid) in enumerate(cards_s):
        acc += (i + 1) * bid
    return acc


def main():
    input = open('input').read().strip()
    # input = open('input_test').read().strip()
    cards = parse_input(input)

    s1 = calc_win(cards, joker=False)
    s2 = calc_win(cards, joker=True)

    print(s1)
    print(s2)


main()
