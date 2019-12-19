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


def check_cell(pos):
    x, y = pos
    inp_que, out_que = Queue(), Queue()
    inp_que.put(x)
    inp_que.put(y)
    run(mem, inp_que.get, out_que.put)
    return bool(out_que.get())


cellmap = {False: '.', True: '#', None: ' '}


def draw(map):
    xmax, ymax = max(x for x, _ in map.keys()), max(y for _, y in map.keys())
    for y in range(ymax + 1):
        l = ''.join(cellmap[map.get((x, y), None)] for x in range(xmax + 1))
        print(l)


def bin_max_search(lb, ub, pred):
    while lb < ub - 1:
        mid = (lb + ub) // 2
        if pred(mid):
            lb = mid
        else:
            ub = mid
    return ub if pred(ub) else lb


def has_square_line(y, width, height):
    reached_beam = False
    for x in it.count():
        reached_beam = reached_beam or check_cell((x, y))
        if reached_beam:
            if not check_cell((x + width - 1, y)):
                return None
            if check_cell((x, y + height - 1)):
                return x


def scan_for_ship(width, height):
    uy = next(
        2 ** ye for ye in it.count(5) if has_square_line(2 ** ye, width, height) != None
    )
    y = (
        bin_max_search(2 ** 4, uy, lambda y: has_square_line(y, width, height) == None)
        + 1
    )
    x = has_square_line(y, width, height)
    return x, y


def scan(width, height):
    map = {pos: check_cell(pos) for pos in it.product(range(width), range(height))}
    return map


def main():
    global mem
    scan_width = scan_height = 50
    ship_width = ship_height = 100
    mem = [int(x) for x in open('input').read().strip().split(',')]

    map = scan(scan_width, scan_height)
    s1 = sum(map.values())

    xship, yship = scan_for_ship(ship_width, ship_height)
    s2 = 10000 * xship + yship

    # draw(map)
    print(s1)
    print(s2)


main()
