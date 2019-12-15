#!/usr/bin/env python3

import operator
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


pixmap = {0: '\u2588', 1: '.', 2: 'X', None: ' '}
dirmap = {(0, -1): 1, (0, 1): 2, (-1, 0): 3, (1, 0): 4}


def draw(map):
    xmin, xmax = min(p[0] for p in map.keys()), max(p[0] for p in map.keys())
    ymin, ymax = min(p[1] for p in map.keys()), max(p[1] for p in map.keys())
    for y in range(ymin, ymax + 1):
        l = ''.join(
            pixmap[map.get((x, y), [None])[0]] if (x, y) != (0, 0) else 'O'
            for x in range(xmin, xmax + 1)
        )
        print(l)


def bfs(map, start):
    freepos = {pos for pos, (t, _) in map.items() if t != 0}
    res = {}
    q = deque([(start, 0)])
    while q:
        pos, dist = q.popleft()
        if pos in res or pos not in freepos:
            continue
        res[pos] = dist
        nbrs = [(add(pos, dir), dist + 1) for dir in dirmap.keys()]
        q.extend(nbrs)
    return res


class ExplorationDone(Exception):
    pass


def test_move(mem, directions):
    if len(directions) == 0:
        return 1

    inp_que, out_que = deque(dirmap[dir] for dir in directions), []

    def out_cb(x):
        out_que.append(x)
        if len(out_que) == len(directions):
            raise ExplorationDone

    try:
        run(mem, inp_que.popleft, out_cb)
    except ExplorationDone:
        pass

    assert 0 not in out_que[:-1]
    return out_que[-1]


def explore(mem, nodraw=True):
    map = {}
    q = deque([((0, 0), [])])
    while q:
        cpos, cpath = q.popleft()
        if cpos in map:
            continue
        type = test_move(mem, cpath)
        map[cpos] = (type, cpath)
        if type == 0:
            continue
        else:
            nbrs = [(add(cpos, dir), cpath + [dir]) for dir in dirmap]
            q.extend(nbrs)

    return map


def main():
    mem = [int(x) for x in open('input').read().strip().split(',')]

    map = explore(mem)
    pos_oxy, s1 = next((pos, len(p)) for pos, (t, p) in map.items() if t == 2)

    oxy_spread = bfs(map, pos_oxy)
    s2 = max(oxy_spread.values())

    draw(map)
    print(s1)
    print(s2)


main()
