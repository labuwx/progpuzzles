#!/usr/bin/env python3

import copy
import re


pattern = re.compile(
    r'(?P<field>.+): (?P<l1>\d+)-(?P<u1>\d+) or (?P<l2>\d+)-(?P<u2>\d+)'
)


def ticket_parser(tt):
    return tuple(int(x) for x in tt.split(','))


def find_bijection(map):
    map = copy.deepcopy(map)
    fixed, change = set(), True
    while change:
        change = False
        for k, v in map.items():
            if len(v) != 1 or k in fixed:
                continue
            fixed.add(k)
            v = next(iter(v))
            for k2, v2 in map.items():
                if k2 != k and v in v2:
                    change = True
                    v2.remove(v)
    map = {k: next(iter(v)) for k, v in map.items()}
    return map


def main():
    input = open('input').read().strip()
    field_desc, my_ticket_txt, other_tickets_txt = input.split('\n\n')

    fields = {
        m['field']: (
            (int(m['l1']), int(m['u1'])),
            (int(m['l2']), int(m['u2'])),
        )
        for l in field_desc.split('\n')
        for m in [pattern.match(l)]
    }

    my_ticket = ticket_parser(my_ticket_txt.split('\n')[1])
    other_tickets = [ticket_parser(l) for l in other_tickets_txt.split('\n')[1:]]

    valid_tickets, error_rate = [], 0
    for t in other_tickets:
        valid = True
        for x in t:
            x_valid = any(
                l1 <= x <= u1 or l2 <= x <= u2 for (l1, u1), (l2, u2) in fields.values()
            )
            valid = valid and x_valid
            if not x_valid:
                error_rate += x
        if valid:
            valid_tickets.append(t)

    matching_fields = {
        i: {
            field
            for field, ((l1, u1), (l2, u2)) in fields.items()
            if all(
                l1 <= t[i] <= u1 or l2 <= t[i] <= u2
                for t in valid_tickets + [my_ticket]
            )
        }
        for i, _ in enumerate(my_ticket)
    }
    bij = find_bijection(matching_fields)

    s2 = 1
    for i, x in enumerate(my_ticket):
        if bij[i].startswith('departure'):
            s2 *= x

    print(error_rate)
    print(s2)


main()
