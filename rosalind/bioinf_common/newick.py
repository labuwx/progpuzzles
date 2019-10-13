import operator
from functools import reduce


def nw_tokenize(nws):
    tokens, s = [], ''
    for c in nws:
        if c in '():,;':
            if s:
                tokens.append(s)
                s = ''
            tokens.append(c)
        else:
            s += c
    if s:
        tokens.append(s)
    return tokens


def from_newick(nws):
    tokens = nw_tokenize(nws)
    nodes = []
    prefix, weights, label, w = [], [], '', None
    for t in tokens:
        if t == '(':
            prefix.append(0)
            weights.append([])
        elif t in '),;':
            if weights:
                weights[-1].append(w if w != None else 1)
            nodes.append((tuple(prefix), tuple(weights), label))
            label = ''
            w = None
            if t == ')':
                prefix.pop()
                weights.pop()
            elif t == ',':
                prefix[-1] += 1
                weights[-1] = []
        elif t == ':':
            w = 0
        elif w != None:
            w = int(t)
        else:
            label = t

    nodes = [
        (prefix, tuple(reduce(operator.add, weights, [])), label)
        for prefix, weights, label in nodes
    ]

    return nodes


def nw_distance(g, l1, l2):
    p1, w1 = next((p, w) for p, w, l in g if l == l1)
    p2, w2 = next((p, w) for p, w, l in g if l == l2)
    plen = next(
        (i for i, (x, y) in enumerate(zip(p1, p2)) if x != y), min(len(p1), len(p2))
    )
    dist = sum(w1[plen:] + w2[plen:])
    return dist
