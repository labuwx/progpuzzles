#!/usr/bin/env python3

from Bio import Entrez

from bioinf_common import *


ds = get_dataset()
name, d1, d2 = ds.split()
# print(name, d1, d2)

Entrez.email = 'your_name@your_mail_server.com'
handle = Entrez.esearch(
    db='nucleotide',
    term=r'"%s"[Organism]' % name,
    datetype='pdat',
    mindate=d1,
    maxdate=d2,
)
record = Entrez.read(handle)

# pprint(record)
print(record['Count'])
