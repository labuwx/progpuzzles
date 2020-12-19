#!/usr/bin/env python3


from collections import deque
import operator

# ordered by higher precedence
opmap = {'+': operator.add, '*': operator.mul}


def tokinze(txt):
    tokens, num = [], ''
    for c in txt:
        if c == ' ':
            pass
        elif c in '0123456789':
            num += c
        else:
            if num != '':
                tokens.append(int(num))
                num = ''
            tokens.append(c)
    if num != '':
        tokens.append(int(num))
    return tokens


def eval_simple(tokens):
    q = deque([None])
    for t in tokens:
        if t in opmap:
            q.append(opmap[t])
        elif t == '(':
            q.append(None)
        else:
            if isinstance(t, int):
                x = t
            else:  # ')'
                x = q.pop()
                q.pop()  # None
            if q[-1] == None:
                q.append(x)
            else:
                op = q.pop()
                a1 = q.pop()
                q.append(op(a1, x))

    assert len(q) == 2
    return q[1]


def eval_hard(tokens):
    outq, opq = deque(), deque()

    for t in tokens + [')']:
        if isinstance(t, int):
            outq.append(t)
        elif t == '(':
            opq.append(t)
        elif t == ')':
            while opq and (op := opq.pop()) != '(':
                a2, a1 = outq.pop(), outq.pop()
                outq.append(opmap[op](a1, a2))
        else:
            while opq and (opq[-1] == '+' or (opq[-1] == '*' and t == '*')):
                op = opq.pop()
                a2, a1 = outq.pop(), outq.pop()
                outq.append(opmap[op](a1, a2))
            opq.append(t)

    assert len(outq) == 1
    return outq[0]


def main():
    input = open('input').read().strip().split('\n')
    tokens = [tokinze(l) for l in input]

    s1 = sum(eval_simple(tks) for tks in tokens)
    s2 = sum(eval_hard(tks) for tks in tokens)

    print(s1)
    print(s2)


main()
