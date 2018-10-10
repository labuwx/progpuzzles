#!/usr/bin/env python3

from bioinf_common import *


prot = get_dataset()
total_weight = sum(monoisotopic_mass_table[aa] for aa in prot)

print(total_weight)
