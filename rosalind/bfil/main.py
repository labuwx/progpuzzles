#!/usr/bin/env python3

from statistics import mean
from Bio import Seq, SeqIO, SeqRecord

from bioinf_common import *


with open(sys.argv[1]) as input:
    q = int(input.readline())
    # records = [rec.letter_annotations['phred_quality'] for rec in SeqIO.parse(input, 'fastq')]
    records = list(SeqIO.parse(input, 'fastq'))

new_records = []
for record in records:
    qual = record.letter_annotations['phred_quality']
    chain = str(record.seq)
    l = len(chain)
    start = next(i for i in range(l) if qual[i] >= q)
    end = next(i for i in range(l - 1, -1, -1) if qual[i] >= q)
    new_chain = chain[start : end + 1]
    new_record = SeqRecord.SeqRecord(
        Seq.Seq(new_chain),
        id=record.id,
        name=record.name,
        description=record.description,
        dbxrefs=record.dbxrefs,
        features=record.features,
        annotations=record.annotations,
        letter_annotations={'phred_quality': qual[start : end + 1]},
    )
    new_records.append(new_record)

SeqIO.write(new_records, 'output.txt', 'fastq')
