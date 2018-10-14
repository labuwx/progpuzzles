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
    if s: tokens.append(s)
    return tokens


def from_newick(nws):
    tokens = nw_tokenize(nws)
    nodes = {}
    prefix, label, w = [], '', None
    for t in tokens:
        if t == '(':
            prefix.append(0)
        elif t in '),;':
            nodes[tuple(prefix)] = (w if w != None else 1, label)
            label = ''
            w = None
            if t == ')':
                prefix.pop()
            elif t == ',':
                prefix[-1] += 1
        elif t == ':':
            w = 0
        elif w != None:
            w = int(t)
        else:
            label = t

    return nodes


def nw_distance(g, u, v):
    # print(u, v)
    p1 = next(n for n, (_, l) in g.items() if l == u)
    p2 = next(n for n, (_, l) in g.items() if l == v)
    # print(p1, p2)
    plen = next((i for i, (x, y) in enumerate(zip(p1, p2)) if x != y), min(len(p1), len(p2)))
    # print(plen)
    dist = sum(
        g[p[:l]][0]
        for p in [p1, p2]
        for l in range(plen+1, len(p)+1)
    )
    return dist
