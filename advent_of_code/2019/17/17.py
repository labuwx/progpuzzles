#!/usr/bin/env python3

import itertools as it
import operator
from collections import defaultdict, deque
from queue import Queue


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


def draw(map):
    for line in map:
        print(line)


dirmap = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}


def turn(dir, r):
    if r == 'R':
        return (dir[1], -dir[0])
    elif r == 'L':
        return (-dir[1], dir[0])
    else:
        return (-dir[0], -dir[1])


def parsemap(map):
    scaffold = set()
    for y, l in enumerate(map):
        for x, c in enumerate(l):
            if c == '#' or c in dirmap.keys():
                pos = (y, x)
                scaffold.add(pos)
                if c in dirmap.keys():
                    robot = (pos, dirmap[c])
    return scaffold, robot


def alignment_score(map):
    scaffold = parsemap(map)[0]
    score = 0
    for y, x in scaffold:
        pos = (y, x)
        if len({add(pos, dir) for dir in dirmap.values()} & scaffold) == 4:
            score += x * y
    return score


def traverse(map):
    scaffold, (pos, dir) = parsemap(map)
    reached = {pos}
    route = []
    while len(reached) < len(scaffold):
        route.append(0)
        while (npos := add(pos, dir)) in scaffold:
            route[-1] += 1
            reached.add(npos)
            pos = npos
        r = 'R' if add(pos, turn(dir, 'R')) in scaffold else 'L'
        route.append(r)
        dir = turn(dir, r)
    route = [cmd for cmd in route if cmd != 0]
    while route[-1] in set('LR'):
        route.pop()
    return route


def do_traverse(mem, cmd):
    mem = mem[:]
    mem[0] = 2

    cmds = {k: (','.join(str(x) for x in c)) for k, c in cmd.items()}
    for c in cmds:
        assert len(c) <= 20
    inp_str = '\n'.join([cmds['main'], cmds['A'], cmds['B'], cmds['C'], 'n']) + '\n'

    inp_que, out_que = deque([ord(x) for x in inp_str]), []
    run(mem, inp_que.popleft, out_que.append)

    return out_que[-1]


def explore(mem):
    out_que = []
    run(mem, None, lambda x: out_que.append(chr(x)))
    map = ''.join(out_que).strip().split()
    return map


def rcompress(route):
    route = list(route)

    sc = it.count()
    newsymb = lambda: '#%d' % next(sc)
    symbols = {}

    while True:
        subs = None
        for i in range(len(route) - 3):
            if subs != None:
                break
            for j in range(i + 2, len(route) - 1):
                if route[i : i + 2] == route[j : j + 2]:
                    subs = route[i : i + 2]
                    break
        if subs == None:
            break

        s = newsymb()
        symbols[s] = subs
        for i in range(len(route) - 2, -1, -1):
            if route[i : i + 2] == subs:
                route[i] = s
                del route[i + 1]

    print()
    print(route)
    print(symbols)
    print()


def main():
    mem = [int(x) for x in open('input').read().strip().split(',')]

    map = explore(mem)
    s1 = alignment_score(map)

    draw(map)

    route = traverse(map)

    print(route)
    # rtrr = rcompress(route)

    rtr = {
        'main': ['A', 'B', 'A', 'C', 'A', 'B', 'C', 'B', 'C', 'A'],
        'A': ['L', 12, 'R', 4, 'R', 4, 'L', 6],
        'B': ['L', 12, 'R', 4, 'R', 4, 'R', 12],
        'C': ['L', 10, 'L', 6, 'R', 4],
    }
    s2 = do_traverse(mem, rtr)

    print(s1)
    print(s2)


main()
