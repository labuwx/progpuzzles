#!/usr/bin/env python3

import itertools as it
import operator
import re
from collections import defaultdict, deque


def add(a, b):
    return tuple(sum(ab) for ab in zip(a, b))


def abs_addr(base, addr, flag):
    return addr + (0 if flag == 0 else base)


def run(mem, inp_cb, out_cb):
    mem = defaultdict(int, enumerate(mem))
    pos, base = 0, 0
    while True:
        pm, opc = mem[pos] // 100, mem[pos] % 100
        if opc == 1:  # add
            op = operator.add
            il, ol = 2, 1
        elif opc == 2:  # mul
            op = operator.mul
            il, ol = 2, 1
        elif opc == 3:  # read
            op = inp_cb
            il, ol = 0, 1
        elif opc == 4:  # print
            op = lambda x: x
            il, ol = 1, 3
        elif opc == 5:  # jump-if-true
            op = lambda c, v: v if c else None
            il, ol = 2, 2
        elif opc == 6:  # jump-if-false
            op = lambda c, v: v if not c else None
            il, ol = 2, 2
        elif opc == 7:  # less than
            op = lambda x, y: int(x < y)
            il, ol = 2, 1
        elif opc == 8:  # equals
            op = lambda x, y: int(x == y)
            il, ol = 2, 1
        elif opc == 9:  # base adjust
            op = lambda x: x
            il, ol = 1, 4
        elif opc == 99:  # halt
            break
        else:
            print('Wrong opc %d at %d' % (opc, pos))
            print(mem)
            exit()

        inp = []
        for _ in range(il):
            v = mem[(pos := pos + 1)]
            f, pm = pm % 10, pm // 10
            inp.append(v if f == 1 else mem[abs_addr(base, v, f)])

        ret = op(*inp)

        if ol == 1:
            f, pm = pm % 10, pm // 10
            mem[abs_addr(base, mem[(pos := pos + 1)], f)] = ret
        pos += 1

        if ol == 2 and ret != None:
            pos = ret

        if ol == 4:
            base += ret

        if ol == 3:
            out_cb(ret)


def clear_script(script):
    script = script.strip().split('\n')
    command_pattern = re.compile(r'^\s*((AND|OR|NOT)\s+\w\s+\w|WALK|RUN)')
    commands = [
        command.groups()[0]
        for line in script
        if (command := next(command_pattern.finditer(line), None)) != None
    ]
    assert len(commands) <= 16
    return commands


def walkrun(mem, script, debug=False):
    inp_que = deque(ord(c) for c in '\n'.join(clear_script(script)) + '\n')
    out_text, res = [], None

    def out_cb(x):
        nonlocal res
        try:
            c = chr(x)
        except ValueError:
            res = x
        else:
            out_text.append(c)

    run(mem, inp_que.popleft, out_cb)

    if res == None and debug:
        print(''.join(out_text))

    return res


def main():
    mem = [int(x) for x in open('input').read().strip().split(',')]
    walkscript = open('walk.spring').read()
    runscript = open('run.spring').read()

    s1 = walkrun(mem, walkscript)
    s2 = walkrun(mem, runscript)

    print(s1)
    print(s2)


main()
