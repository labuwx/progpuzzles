#!/usr/bin/env python3

from Bio import SeqIO

from bioinf_common import *


with open(sys.argv[1]) as input, open('output.txt', 'w') as output:
    SeqIO.convert(input, 'fastq', output, 'fasta')
