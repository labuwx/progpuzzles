#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
dna = list(from_fasta(ds).values())[0]

j, failure_array = 0, [0]
for c in dna[1:]:
    while j > 0 and dna[j] != c:
        j = failure_array[j-1]
    if dna[j] == c: j += 1
    failure_array.append(j)

print(*failure_array)
