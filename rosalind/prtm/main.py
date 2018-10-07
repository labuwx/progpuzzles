#!/usr/bin/env python3

from bioinf_common import *


prots = get_dataset()
total_weight = sum(monoisotopic_mass_table[p] for p in prots)

print(total_weight)
