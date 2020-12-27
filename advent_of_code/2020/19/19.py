#!/usr/bin/env python3

from collections import defaultdict
import copy
import itertools as it

# runtime: ~30 min


def parse_rule(txt):
    tokens = txt.split()
    id = int(tokens[0][:-1])
    l = [[]]
    for t in tokens[1:]:
        if t == '|':
            l.append([])
        elif t[0] == '"':
            l[-1].append(t[1:-1])
        else:
            l[-1].append(int(t))
    return (id, l)


def match(rules, msg):
    mem = defaultdict(bool)
    n = len(msg)

    for (i, c), (id, rls) in it.product(enumerate(msg), rules.items()):
        for rule in rls:
            if rule[0] == c:
                assert len(rule) == 1
                mem[(1, i, id)] = True

    for l in range(2, n + 1):
        for i, p, (id, rls) in it.product(range(n - l + 1), range(1, l), rules.items()):
            for rule in (r for r in rls if len(r) == 2):
                id1, id2 = rule
                if mem[p, i, id1] and mem[l - p, i + p, id2]:
                    mem[l, i, id] = True
                    break

    return mem[n, 0, 0]


# partial Chomsky normal form (TERM, BIN, UNIT)
def convto_cnf(rules):
    id_gen = it.count(max(rules.keys()) + 1)
    out_rules = defaultdict(list)
    for id, rls in rules.items():
        for rules in rls:
            # TERM
            if len(rules) > 1:
                rules = list(rules)
                for i in range(len(rules)):
                    t = rules[i]
                    if isinstance(t, str):
                        tmp_id = next(id_gen)
                        out_rules[tmp_id] = [[t]]
                        rules[i] = tmp_id

            # BIN
            curr_id = id
            while len(rules) > 2:
                next_id = next(id_gen)
                out_rules[curr_id].append([rules[0], next_id])
                rules = rules[1:]
                curr_id = next_id
            out_rules[curr_id].append(rules)

    # UNIT
    for rls in out_rules.values():
        i = 0
        while i < len(rls):
            if len(rls[i]) == 1 and isinstance(rls[i][0], int):
                rls += out_rules[rls[i][0]]
                del rls[i]
            else:
                i += 1

    return out_rules


def main():
    input = open('input').read().strip().split('\n\n')
    rules_orig = dict(parse_rule(l) for l in input[0].split('\n'))
    messages = input[1].split()

    rules1 = convto_cnf(rules_orig)
    s1 = sum(match(rules1, msg) for msg in messages)

    rules_orig_2 = copy.deepcopy(rules_orig)
    rules_orig_2.update({8: [[42], [42, 8]], 11: [[42, 31], [42, 11, 31]]})
    rules2 = convto_cnf(rules_orig_2)
    s2 = sum(match(rules2, msg) for msg in messages)

    print(s1)
    print(s2)


main()
