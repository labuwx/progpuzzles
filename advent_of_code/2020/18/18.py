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
    q = deque(tokens + [None])

    plevel = 0
    while (t := q.popleft()) != None:
        if t == '(':
            if plevel == 0:
                sub_expr = []
            else:
                sub_expr.append(t)
            plevel += 1
        elif t == ')':
            plevel -= 1
            if plevel == 0:
                q.append(eval_hard(sub_expr))
            else:
                sub_expr.append(t)
        else:
            (q if plevel == 0 else sub_expr).append(t)

    for opt, op in opmap.items():
        q.append(None)
        while (t := q.popleft()) != None:
            if t == opt:
                q.append(op(q.pop(), q.popleft()))
            else:
                q.append(t)

    return q[0]


def main():
    input = open('input').read().strip().split('\n')
    tokens = [tokinze(l) for l in input]

    s1 = sum(eval_simple(tks) for tks in tokens)
    s2 = sum(eval_hard(tks) for tks in tokens)

    print(s1)
    print(s2)


main()
