#!/usr/bin/env python3

from Bio import Entrez, SeqIO, pairwise2

from bioinf_common import *


ds = get_dataset().split()

Entrez.email = 'your_name@your_mail_server.com'
handle = Entrez.efetch(db='nucleotide', id=ds, rettype='fasta')
records = list(SeqIO.parse(handle, 'fasta'))
c1, c2 = [str(rec.seq) for rec in records]

alignments = pairwise2.align.globalms(c1, c2, 5, -4, -10, -1)
score = int(max(alignments, key=lambda x: x[2])[2])

print(score)
