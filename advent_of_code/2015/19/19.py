#!/usr/bin/env python3


from collections import defaultdict
import itertools as it
import re


mol_pattern = re.compile(r'[A-Z][a-z]*')


def split_mol(mol):
    return tuple(mol_pattern.findall(mol))


def one_reach(rules, molecule):
    if molecule == ('e',):
        return set(rules['e'])

    new_molecules = set()
    for i, elem in enumerate(molecule):
        for mol in rules[elem]:
            new_mol = molecule[:i] + mol + molecule[i + 1 :]
            new_molecules.add(new_mol)
    return new_molecules


def subi(sub, arr):
    l = len(sub)
    i = next((i for i in range(len(arr) - l + 1) if sub == arr[i : i + l]), None)
    return i, l


def main():
    input = open('input').read().strip().split('\n')

    medicine = split_mol(input[-1])

    # if 2nd part breaks, sort rev_rules: big molecules first
    rules, rev_rules = defaultdict(set), {}
    for l in input[:-2]:
        m1, _, m2 = l.split()
        m2 = split_mol(m2)
        rules[m1].add(m2)
        rev_rules[m2] = m1

    s1 = len(one_reach(rules, medicine))

    work_mol = medicine
    for n in it.count():
        if work_mol == ('e',):
            s2 = n
            break
        mol, revmol = next(
            (mol, revmol)
            for mol, revmol in rev_rules.items()
            if subi(mol, work_mol)[0] != None
        )
        i, l = subi(mol, work_mol)
        work_mol = work_mol[:i] + (revmol,) + work_mol[i + l :]

    print(s1)
    print(s2)


main()
