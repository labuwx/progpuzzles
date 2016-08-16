#!/usr/bin/env python3

from pphelp import *


#N = 3
#M = 5
#K = 2
N = 13000
M = 13000
K =30

s = N*K*M % 1009
e1, e2, e3 = s, 1237, 345892
g = nx.DiGraph()
g.add_node('A')

seqs = []
for n in range(0, N):
    seq = []
    for m in range(1, M+1):
        val = e1 % K
        seq.append(val)
        v =  (31*e1 + 103*e2 + 7*e3 + 500003) % 1000001
        e1, e2, e3 = e2, e3, v
        g.add_node((n, m))
        if n > 0 and seqs[0][m-1] == val:
            if m > 1:
                g.add_edge((n, m-1), (n, m), weight=0)
                g.add_edge((0, m-1), (n, m), weight=1)
            else:
                g.add_edge('A', (n, m), weight=1)
            g.add_edge((n, m), (0, m), weight=0)
    seqs.append(seq)





pprint(g.number_of_nodes())
pprint(g.number_of_edges())

l = nx.shortest_path_length(g, 'A', (0,M), weight='weight')
print(l)

