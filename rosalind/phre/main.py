#!/usr/bin/env python3

from statistics import mean
from Bio import SeqIO

from bioinf_common import *


with open(sys.argv[1]) as input:
    threshold = int(input.readline())
    records = list(SeqIO.parse(input, 'fastq'))

low_q = sum(1 for rec in records if mean(rec.letter_annotations['phred_quality']) < threshold)

print(low_q)
