import math
import re
import requests
import sys
import itertools as it
from collections import OrderedDict

from .maps import *


def get_dataset():
    ds = open(sys.argv[1]).read().strip()
    ds = '\n'.join(line.strip() for line in ds.split('\n'))
    return ds


def dna2rna(dna):
    return dna.replace('T', 'U')


def rna2dna(rna):
    return rna.replace('U', 'T')


def rev_comp(dna):
    return ''.join(base_pairs[b] for b in reversed(dna))


def gc_cont(xna):
    gcs = sum(1 for x in xna if x in ['C', 'G'])
    return gcs / len(xna) * 100


def get_profile(dna_l):
    l = len(dna_l[0])
    profile = {
        b: [sum(1 for dna in dna_l if dna[i] == b) for i in range(l)]
        for b in set(base_pairs.values())
    }
    return profile


def get_consensus(profile):
    l = len(list(profile.values())[0])
    consensus = [
        max(profile.items(), key=lambda x: x[1][i])[0]
        for i in range(l)
    ]
    return consensus


def rna2prots(rna, strict_mode=False):
    prots = ''
    stopped = not strict_mode
    for i in range(0, len(rna)//3):
        codon = rna[3*i: 3*i+3]
        prot = codon_map[codon]
        if prot is None:
            if strict_mode:
                stopped = True
                break
            else:
                continue
        prots += prot
    return prots if stopped else None


def get_orf(rna):
    pattern = r'(?=%s)' % prot_rna_pattern
    orf_l = [m.group('orf') for m in re.finditer(pattern, rna)]
    return orf_l


def get_exons(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, '')
    return dna


def hamm_dist(s1, s2):
    return sum(1 for a, b in it.zip_longest(s1, s2) if a != b)


def pmotif_search(pattern, chain=None):
    re_pattern = r'(?=%s)' % pattern.replace('{', '[^').replace('}', ']')
    matcher = re.compile(re_pattern)

    def find_motif(chain):
        idx = [m.start()+1 for m in matcher.finditer(chain)]
        return idx

    if chain is None:
        return find_motif
    else:
        return find_motif(chain)


def from_fasta(s):
    s = s.strip()
    d = []
    for line in s.split('\n'):
        line = line.strip()
        if line == '' or line.startswith(';'):
            continue
        elif line.startswith('>'):
            id = line[1:].split()[0]
            id_sp = id.split('|')
            if len(id_sp) > 1:
                id = id_sp[1]
            d.append([id, ''])
        else:
            d[-1][1] += line
    return OrderedDict(d)


def from_uniprot(ids):
    url_base = r'https://www.uniprot.org/uniprot/%s.fasta'
    txt = '\n'.join(requests.get(url_base % id).text for id in ids)
    prots = from_fasta(txt)
    return prots


def nCr(n,r=2):
    f = math.factorial
    return f(n) // f(r) // f(n-r)
