#!/usr/bin/env python3

import operator
import regex as re
from collections import defaultdict


s2op = {
    '==': operator.eq,
    '!=': operator.ne,
    '<': operator.lt,
    '<=': operator.le,
    '>=': operator.ge,
    '>': operator.gt,
}


input = open('input').read()

mem = defaultdict(int)
global_max = 0
for line in input.split('\n'):
    if line == '':
        continue
    m = re.match(
        r'^(?P<target>\w+) (?P<op>inc|dec) (?P<amount>-?\d+) if (?P<condreg>\w+) (?P<condop>==|!=|<|>|<=|>=) (?P<condvalue>-?\d+)$',
        line,
    )

    if s2op[m.group('condop')](mem[m.group('condreg')], int(m.group('condvalue'))):
        amount = int(m.group('amount'))
        target = m.group('target')
        new_value = mem[target] + (amount if m.group('op') == 'inc' else -amount)
        mem[target] = new_value
        global_max = max(global_max, new_value)

print(max(mem.values()))
print(global_max)
