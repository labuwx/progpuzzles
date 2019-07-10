#!/usr/bin/env python3

import itertools as it

def gen_amt(b, m):
    amt = {}
    for x, y in it.product(range(m), repeat=2):
        ds = [d for d in range(b) if (x*b+d) % m == y]
        if ds:
            amt[(x, y)] = '|'.join(str(d) for d in ds)  
    return amt

def rem_st(amt, st):
    ss = {s[i] for s in amt.keys() for i in range(2)}
    namt = {}
    for (x, y) in it.product(ss, repeat=2):
        if st in (x, y): continue
        t0 = amt.get((x, y), None)
        t1 = amt.get((x, st), None)
        t2 = amt.get((st, st), None)
        t3 = amt.get((st, y), None)
        if None not in (t1, t3):
            t1 = (r'(?:' + t1 + r')') if '|' in t1 else t1
            t3 = (r'(?:' + t3 + r')') if '|' in t3 else t3
            if t2:
                tt = t1 + r'(?:' + t2 + r')*?' + t3
            else:
                tt = t1 + t3
        else:
            tt = None

        if tt and t0:
            t0 = (r'(?:' + t0 + r')') if '|' in t0 else t0
            tt = (r'(?:' + tt + r')') if '|' in tt else tt
            tn = t0 + r'|' + tt
        elif tt:
            tn = tt
        elif t0:
            tn = t0
        else:
            continue
        namt[(x, y)] = tn
    return namt


def regex_divisible_by(m):
    b = 2
    amt = gen_amt(b, m)
    for k in range(1, m):
        amt = rem_st(amt, k)
    rx = r'^(?:' + amt[(0, 0)] + r')+$'
    return rx

print(regex_divisible_by(3))
