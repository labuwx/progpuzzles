#!/usr/bin/env python3

from itertools import count
from infinite import product
import operator


def run(mem):
    pos = 0
    while True:
        opc = mem[pos]
        if opc == 1:
            op = operator.add
        elif opc == 2:
            op = operator.mul
        elif opc == 99:
            break
        else:
            raise 'Wrong opc'

        ia, ib, ic = mem[pos+1], mem[pos+2], mem[pos+3]
        mem[ic] = op(mem[ia], mem[ib])
        pos += 4
    return mem

def eval(mem, noun, verb):
    mem = list(mem)
    mem[1], mem[2] = noun, verb
    return run(mem)[0]

def search(res, mem):
    for noun, verb in product(count(0), count(0)):
        if eval(mem, noun, verb) == res:
            return (noun, verb)


input = open('input').read()
input = [int(x) for x in input.split(',')]

s1 = eval(input, 12, 2)
s2 = search(19690720, input)
s2 = 100 * s2[0] + s2[1]

print(s1)
print(s2)
