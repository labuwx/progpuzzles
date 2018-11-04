#!/usr/bin/env python3

from Bio.Seq import Seq

from bioinf_common import *


ds = get_dataset()
dna = Seq(ds)

print(*(dna.count(b) for b in ('A', 'C', 'G', 'T')))
