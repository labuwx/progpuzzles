#!/usr/bin/env python3

import operator
import os
from collections import defaultdict
from time import sleep


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

    return mem


pixmap = {0: ' ', 1: '|', 2: '#', 3: '-', 4: '*'}


def draw(img, score):
    os.system('clear')
    print(score)
    xmax = max(p[0] for p, v in img.items() if v != 0)
    ymax = max(p[1] for p, v in img.items() if v != 0)
    for y in range(ymax + 1):
        l = ''.join(pixmap[img[(x, y)]] for x in range(xmax + 1))
        print(l)


def count_blocks(img):
    return sum(t == 2 for t in img.values())


def play(mem, nodraw=True):
    img = defaultdict(int)
    score = 0
    tmp = []

    def out_cb(x):
        nonlocal tmp, score
        tmp.append(x)
        if len(tmp) == 3:
            pos, v = (tmp[0], tmp[1]), tmp[2]
            if pos == (-1, 0):
                score = v
            else:
                img[pos] = v
            tmp = []

    def inp_cb():
        xball = next(p[0] for p, v in img.items() if v == 4)
        xpaddle = next(p[0] for p, v in img.items() if v == 3)
        move = xball - xpaddle
        if abs(move) > 1:
            move //= abs(move)
        if not nodraw:
            draw(img, score)
            sleep(0.1)
        return move

    run(mem, inp_cb, out_cb)
    return score, img


def main():
    mem = [int(x) for x in open('input').read().strip().split(',')]

    img1 = play(mem)[1]
    s1 = count_blocks(img1)

    mem = list(mem)
    mem[0] = 2
    s2, img2 = play(mem)
    assert count_blocks(img2) == 0

    print(s1)
    print(s2)


main()
