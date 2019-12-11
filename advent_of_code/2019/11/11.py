#!/usr/bin/env python3

import operator
from collections import defaultdict


def abs_addr(base, addr, flag):
    return addr + (0 if flag == 0 else base)


def turn(cdir, f):
    if f == 0:
        f = -1
    return (f * cdir[1], -f * cdir[0])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


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

    return mem


def paint(mem, sc):
    panels = defaultdict(lambda: (0, False), {(0, 0): (sc, False)})
    ppos, dir, outp = (0, 0), (-1, 0), 0
    inp_cb = lambda: panels[ppos][0]

    def out_cb(x):
        nonlocal outp, ppos, dir
        if outp:
            dir = turn(dir, x)
            ppos = add(ppos, dir)
        else:
            panels[ppos] = (x, True)
        outp = (outp + 1) % 2

    run(mem, inp_cb, out_cb)
    return panels


def draw(panels):
    ymin = ymax = xmin = xmax = 0
    for (y, x), (c, _) in panels.items():
        if not c:
            continue
        ymin, ymax = min(ymin, y), max(ymax, y)
        xmin, xmax = min(xmin, x), max(xmax, x)
    for y in range(ymin, ymax + 1):
        l = ''
        for x in range(xmin, xmax + 1):
            l += '#' if panels[(y, x)][0] else ' '
        print(l)


def main():
    mem = [int(x) for x in open('input').read().strip().split(',')]

    panels1 = paint(mem, 0)
    s1 = sum(t for _, t in panels1.values())

    panels2 = paint(mem, 1)

    print(s1)
    draw(panels2)


main()
