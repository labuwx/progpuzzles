#!/usr/bin/env python3

import sys
from collections import deque

e_8 = 2 ** 8
e_15 = 2 ** 15

# program = [9, 32768, 32769, 4, 19, 32768]

program = []
with open('challenge.bin', 'rb') as f:
    while True:
        word = f.read(2)
        if len(word) == 0:
            break
        word = word[1] * e_8 + word[0]
        program.append(word)


def gnum():
    global ip
    v = memory[ip]
    ip += 1
    return v


def gval():
    v = gnum()
    if v < e_15:
        return v
    else:
        return regs[v - e_15]


def greg():
    return gnum() - e_15


### stack ###
stack = deque()


def push(x):
    stack.append(x)


def pop():
    x = stack.pop()
    return x


#############

regs = [0] * 8
memory = [0] * e_15
for p, x in enumerate(program):
    memory[p] = x

inp_buf = deque()


def inp():
    if len(inp_buf) == 0:
        inp_str = input() + '\n'
        inp_buf.extend(inp_str)
    c = inp_buf.popleft()
    return ord(c)


ip = 0
while ip < len(memory):
    op = memory[ip]
    ip += 1

    if op == 0:  # halt
        break
    elif op == 1:  # set
        a = greg()
        b = gval()
        regs[a] = b
    elif op == 2:  # push
        a = gval()
        push(a)
    elif op == 3:  # pop
        a = greg()
        regs[a] = pop()
    elif op == 4:  # eq
        a = greg()
        b = gval()
        c = gval()
        regs[a] = 1 if b == c else 0
    elif op == 5:  # gt
        a = greg()
        b = gval()
        c = gval()
        regs[a] = 1 if b > c else 0
    elif op == 6:  # jmp
        a = gval()
        ip = a
    elif op == 7:  # jt
        a = gval()
        b = gval()
        if a != 0:
            ip = b
    elif op == 8:  # jf
        a = gval()
        b = gval()
        if a == 0:
            ip = b
    elif op == 9:  # add
        a = greg()
        b = gval()
        c = gval()
        regs[a] = (b + c) % e_15
    elif op == 10:  # mult
        a = greg()
        b = gval()
        c = gval()
        regs[a] = (b * c) % e_15
    elif op == 11:  # mod
        a = greg()
        b = gval()
        c = gval()
        regs[a] = b % c
    elif op == 12:  # and
        a = greg()
        b = gval()
        c = gval()
        regs[a] = b & c
    elif op == 13:  # or
        a = greg()
        b = gval()
        c = gval()
        regs[a] = b | c
    elif op == 14:  # not
        a = greg()
        b = gval()
        regs[a] = ~b + e_15
    elif op == 15:  # rmem
        a = greg()
        b = gval()
        regs[a] = memory[b]
    elif op == 16:  # wmem
        a = gval()
        b = gval()
        memory[a] = b
    elif op == 17:  # call
        a = gval()
        push(ip)
        ip = a
    elif op == 18:  # ret
        try:
            v = pop()
        except:
            break
        ip = v
    elif op == 19:  # out
        a = gval()
        # print(a)
        print(chr(a), end='')
    elif op == 20:  # in
        a = greg()
        regs[a] = inp()
    elif op == 21:  # noop
        pass
    else:
        assert False
