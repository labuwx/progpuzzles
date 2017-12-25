#!/usr/bin/env python3

from collections import defaultdict


trans = {
    ('A', 0): (1, 'R', 'B'),
    ('A', 1): (0, 'L', 'B'),
    ('B', 0): (0, 'R', 'C'),
    ('B', 1): (1, 'L', 'B'),
    ('C', 0): (1, 'R', 'D'),
    ('C', 1): (0, 'L', 'A'),
    ('D', 0): (1, 'L', 'E'),
    ('D', 1): (1, 'L', 'F'),
    ('E', 0): (1, 'L', 'A'),
    ('E', 1): (0, 'L', 'D'),
    ('F', 0): (1, 'R', 'A'),
    ('F', 1): (1, 'L', 'E'),
}

state = 'A'
idx = 0
tape = defaultdict(int)
for _ in range(12629077):
    b = tape[idx]
    b, move, state = trans[(state, b)]
    tape[idx] = b
    idx += 1 if move == 'R' else -1

checksum = sum(tape.values())
print(checksum)
