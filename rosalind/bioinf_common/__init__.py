import math
import re
import requests
import sys
import itertools as it
from collections import defaultdict, deque, OrderedDict
pprint = __import__('pprint').PrettyPrinter().pprint

from .maps import *
from .newick import from_newick, nw_distance


def get_dataset():
    ds = open(sys.argv[1]).read().strip()
    ds = '\n'.join(line.strip() for line in ds.split('\n'))
    return ds


def dna2rna(dna):
    return dna.replace('T', 'U')


def rna2dna(rna):
    return rna.replace('U', 'T')


def rev_comp(dna):
    return ''.join(base_pairs[b] for b in reversed(dna))


def rev_comp_rna(rna):
    return ''.join(base_pairs_rna[b] for b in reversed(rna))


def gc_cont(xna):
    gcs = sum(1 for x in xna if x in ['C', 'G'])
    return gcs / len(xna) * 100


def get_profile(dna_l):
    l = len(dna_l[0])
    profile = {
        b: [sum(1 for dna in dna_l if dna[i] == b) for i in range(l)]
        for b in set(base_pairs.values())
    }
    return profile


def get_consensus(profile):
    l = len(list(profile.values())[0])
    consensus = [
        max(profile.items(), key=lambda x: x[1][i])[0]
        for i in range(l)
    ]
    return consensus


def rna2prot(rna, strict_mode=False):
    prot = ''
    stopped = not strict_mode
    for i in range(0, len(rna)//3):
        codon = rna[3*i: 3*i+3]
        aa = codon_map[codon]
        if aa is None:
            if strict_mode:
                stopped = True
                break
            else:
                continue
        prot += aa
    return prot if stopped else None


def get_orf(rna):
    pattern = r'(?=%s)' % prot_rna_pattern
    orf_l = [m.group('orf') for m in re.finditer(pattern, rna)]
    return orf_l


def get_exons(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, '')
    return dna


def hamm_dist(s1, s2):
    return sum(1 for a, b in it.zip_longest(s1, s2) if a != b)


def trans_type(b1, b2):
    if b1 == b2:
        return None
    elif len({b1, b2} & {'A', 'G'}) % 2 == 0:
        return 'TI'
    else:
        return 'TV'


def tt_ratio(dna1, dna2):
    ts = [trans_type(b1, b2) for b1, b2 in zip(dna1, dna2)]
    r = ts.count('TI') / ts.count('TV')
    return r


def pmotif_search(pattern, chain=None):
    re_pattern = r'(?=%s)' % pattern.replace('{', '[^').replace('}', ']')
    matcher = re.compile(re_pattern)

    def find_motif(chain):
        idx = [m.start()+1 for m in matcher.finditer(chain)]
        return idx

    if chain is None:
        return find_motif
    else:
        return find_motif(chain)


def from_fasta(s):
    s = s.strip()
    d = []
    for line in s.split('\n'):
        line = line.strip()
        if line == '' or line.startswith(';'):
            continue
        elif line.startswith('>'):
            id = line[1:].split()[0]
            id_sp = id.split('|')
            if len(id_sp) > 1:
                id = id_sp[1]
            d.append([id, ''])
        else:
            d[-1][1] += line
    return OrderedDict(d)


def from_uniprot(ids):
    url_base = r'https://www.uniprot.org/uniprot/%s.fasta'
    txt = '\n'.join(requests.get(url_base % id).text for id in ids)
    prots = from_fasta(txt)
    return prots


def nCr(n, r=2):
    f = math.factorial
    return f(n) // f(r) // f(n-r)


def dfs(nodes, edges):
    parent, reached, left, etype = {}, {}, {}, {}
    rn, ln = it.count(), it.count()
    for v0 in nodes:
        if v0 in reached:
            continue

        q, branch = [(None, v0)], []
        while q:
            p, u = q.pop()
            if u in reached: continue
            parent[u] = p
            reached[u] = next(rn)

            while branch and branch[-1] != p:
                left[branch.pop()] = next(ln)
            branch.append(u)

            for e in (e for e in edges if e[0] == u):
                v = e[1]
                if v not in reached:
                    q.append((u, v))
                    etype[e] = 'T'
                elif v not in left:
                    etype[e] = 'R'
                else:
                    etype[e] = 'F' if reached[u] < reached[v] else 'X'

        while branch:
            left[branch.pop()] = next(ln)

    return parent, reached, left, etype


def topo_sort_dfs(nodes, edges):
    left = dfs(nodes, edges)[2]
    topo_order = sorted(left.keys(), key=left.get, reverse=True)
    return topo_order


def topo_sort(nodes, edg):
    start_node = 'S_T_A_R_T__N_O_D_E'
    edge = lambda x, y: x == start_node or edg(x, y)
    seen, branch, left = set(), deque(), deque()
    q = deque([start_node])
    while q:
        v = q.pop()
        if v in seen: continue
        seen.add(v)
        q.extend(x for x in nodes if edge(v, x))

        while branch and v not in (x for x in nodes if edge(branch[-1], x)):
            left.append(branch.pop())
        branch.append(v)
    return list(branch)[1:] + list(left)[::-1]


def lcsq(a, b):
    a, b = list(a), list(b)
    l, m = len(a), len(b)
    cache = defaultdict(lambda: (0, -1, -1))
    idxs = it.product(range(l), range(m))
    for i, j in idxs:
        if a[i] == b[j]:
            val = (cache[(i-1, j-1)][0] + 1, i-1, j-1)
        else:
            val = max([
                (cache[(i-1, j)][0], i-1, j),
                (cache[(i, j-1)][0], i, j-1)
            ], key=lambda v: v[0])
        cache[(i, j)] = val

    ss = []
    i, j = l-1, m-1
    while i > -1 and j > -1:
        ca, cb = a[i], b[j]
        l, i, j = cache[(i, j)]
        if ca == cb:
            ss.append(ca)
    ss = list(reversed(ss))

    return ss


def longest_mon_subseq(s, decreasing=False, strict=False):
    s2 = set(s) if strict else s
    s2 = sorted(s2, reverse=decreasing)
    return lcsq(s, s2)


def scsq(a, b):
    subs = lcsq(a, b)
    supers = []

    for c in subs:
        i, j = a.index(c), b.index(c)
        supers += a[:i] + b[:j] + c
        a, b = a[i+1:], b[j+1:]
    supers += [a, b]

    return supers


def edit_distance(a, b):
    l, m = len(a), len(b)
    cache = defaultdict(int)
    idxs = sorted(it.product(range(-1, l), range(-1, m)), key=sum)
    for i, j in idxs:
        if i == -1 or j == -1:
            val = i + j + 2
        else:
            ca, cb = a[i], b[j]
            if ca == cb:
                val = cache[(i-1, j-1)]
            else:
                val = min(
                    cache[(i-1, j)],
                    cache[(i, j-1)],
                    cache[(i-1, j-1)]
                ) + 1
        cache[(i, j)] = val

    return cache[l-1, m-1]


def from_edgelist(txt):
    lines = [l for l in reversed(txt.split('\n')) if l]
    ng = int(lines.pop()) if len(lines[-1].split()) == 1 else None
    graphs = []
    for _ in range(ng if ng != None else 1):
        n, m = (int(x) for x in lines.pop().split())
        edges = [tuple(int(x) for x in lines.pop().split()) for __ in range(m)]
        nodes = set(range(1, n+1))
        graphs.append((nodes, edges)) 

    assert(lines == [])
    return graphs if ng != None else graphs[0]


def bellman_ford(nodes, edges, start):
    edges = sorted(edges, key=lambda e: e[0])
    dist = defaultdict(lambda: math.inf, {start: 0})
    parent = {}
    for _ in range(len(nodes)-1):
        for u, v, c in edges:
            if dist[u] + c < dist[v]:
                parent[v] = u
                dist[v] = dist[u] + c

    for u, v, c in edges:
        if dist[u] + c < dist[v]:
            return None

    return dist
