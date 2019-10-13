with open('p107_network.txt') as netwf:
    am = [
        [(None if val == '-' else int(val)) for val in line[:-1].split(',')]
        for line in netwf.readlines()
    ]

N = len(am)

edges = []

for u in range(N):
    for v in range(N):
        if am[u, v]:
            edges.append(sorted([u, v]))
