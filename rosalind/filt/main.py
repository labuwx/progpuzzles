#!/usr/bin/env python3

from statistics import mean
from Bio import SeqIO

from bioinf_common import *


with open(sys.argv[1]) as input:
    q, p = (int(x) for x in input.readline().split())
    records_q = [rec.letter_annotations['phred_quality'] for rec in SeqIO.parse(input, 'fastq')]

n = 0
for qual in records_q:
    qual_f = [x for x in qual if x >= q]
    if len(qual_f) >= len(qual) * p / 100:
        n += 1

print(n)
