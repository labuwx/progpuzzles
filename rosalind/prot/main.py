#!/usr/bin/env python3

from bioinf_common import *


rna = get_dataset()
prot = rna2prot(rna)

print(prot)
