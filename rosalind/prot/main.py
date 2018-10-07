#!/usr/bin/env python3

from bioinf_common import *


rna = get_dataset()
prots = rna2prots(rna)

print(prots)
