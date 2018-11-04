#!/usr/bin/env python3

from Bio import Entrez, SeqIO

from bioinf_common import *


ds = get_dataset().split()

Entrez.email = 'your_name@your_mail_server.com'
handle = Entrez.efetch(db='nucleotide', id=ds, rettype='fasta')
records = list(SeqIO.parse(handle, 'fasta'))

res = min(records, key=lambda x: len(x.seq))

print(res.format('fasta'))
