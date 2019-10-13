#!/usr/bin/env python3

from statistics import mean
from Bio import SeqIO

from bioinf_common import *


with open(sys.argv[1]) as input:
    q = int(input.readline())
    records_q = [
        rec.letter_annotations['phred_quality'] for rec in SeqIO.parse(input, 'fastq')
    ]

low_qt = sum(
    1 for i in range(len(records_q[0])) if mean(rec[i] for rec in records_q) < q
)

print(low_qt)
