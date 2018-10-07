#!/usr/bin/env python3

from collections import Counter

from bioinf_common import *


dna = get_dataset()
cnt = Counter(dna)

print(cnt['A'], cnt['C'], cnt['G'], cnt['T'])
