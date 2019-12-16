#!/usr/bin/env python3

import operator
from collections import defaultdict, deque
import asyncio
from asyncio import Queue


def add(a, b):
    return tuple(sum(ab) for ab in zip(a, b))


def abs_addr(base, addr, flag):
    return addr + (0 if flag == 0 else base)


def inv(a):
    return tuple(-ai for ai in a)


def getdir(ffrom, tto):
    return tuple(ti - fi for fi, ti in zip(ffrom, tto))


async def run(mem, inp_cb, out_cb):
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

        if asyncio.iscoroutinefunction(op):
            ret = await op(*inp)
        else:
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
            await out_cb(ret)


pixmap = {0: '\u2588', 1: '.', 2: 'X', None: ' '}
dirmap = {(0, -1): 1, (0, 1): 2, (-1, 0): 3, (1, 0): 4}


def draw(map):
    xmin, xmax = min(p[0] for p in map.keys()), max(p[0] for p in map.keys())
    ymin, ymax = min(p[1] for p in map.keys()), max(p[1] for p in map.keys())
    for y in range(ymin, ymax + 1):
        l = ''.join(
            pixmap[map.get((x, y), None)] if (x, y) != (0, 0) else 'O'
            for x in range(xmin, xmax + 1)
        )
        print(l)


def bfs(map, start):
    freepos = {pos for pos, t in map.items() if t != 0}
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


async def explore(mem, nodraw=True):
    inp_que, out_que = Queue(), Queue()
    robot = asyncio.Task(run(mem, inp_que.get, out_que.put))

    async def move(dir):
        await inp_que.put(dirmap[dir])
        res = await out_que.get()
        return res

    async def dfs():
        map = {(0, 0): 1}
        q, branch = [((0, 0), dir) for dir in dirmap], [((0, 0), None)]
        while q:
            p, u = q.pop()
            if u in map:
                continue

            while branch[-1][0] != p:
                await move(inv(branch.pop()[1]))

            dir = getdir(p, u)
            type = await move(dir)
            map[u] = type

            if type == 0:
                continue

            branch.append((u, dir))

            nbrs = (add(u, dir) for dir in dirmap)
            q.extend((u, v) for v in nbrs if v not in map)
        return map

    dfs_task = asyncio.Task(dfs())

    await asyncio.wait([dfs_task, robot], return_when=asyncio.FIRST_COMPLETED)
    return dfs_task.result()


def main():
    mem = [int(x) for x in open('input').read().strip().split(',')]

    map = asyncio.run(explore(mem))
    pos_oxy = next(pos for pos, t in map.items() if t == 2)
    s1 = bfs(map, (0, 0))[pos_oxy]

    oxy_spread = bfs(map, pos_oxy)
    s2 = max(oxy_spread.values())

    draw(map)
    print(s1)
    print(s2)


main()
