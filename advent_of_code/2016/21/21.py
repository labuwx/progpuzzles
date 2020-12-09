#!/usr/bin/env python3

from collections import deque
import re


pattern = re.compile(
    r'''(?P<swpos>swap\ position\ (?P<swpos1>\d+)\ with\ position\ (?P<swpos2>\d+)) |
        (?P<swlet>swap\ letter\ (?P<letter1>\w)\ with\ letter\ (?P<letter2>\w)) |
        (?P<rotdir>rotate\ (?P<dir>left|right)\ (?P<nstep>\d+)\ steps?) |
        (?P<rotpos>rotate\ based\ on\ position\ of\ letter\ (?P<letter>\w)) |
        (?P<rev>reverse\ positions\ (?P<revpos1>\d+)\ through\ (?P<revpos2>\d+)) |
        (?P<move>move\ position\ (?P<mvpos1>\d+)\ to\ position\ (?P<mvpos2>\d+))''',
    flags=re.VERBOSE,
)


def scramble(instr, s, unscramble=False):
    instr = reversed(instr) if unscramble else instr
    s = deque(s)
    for cmd, a1, a2 in instr:
        if cmd == 'swpos':
            s[a1], s[a2] = s[a2], s[a1]
        elif cmd == 'swlet':
            i1, i2 = s.index(a1), s.index(a2)
            s[i1], s[i2] = a2, a1
        elif cmd == 'rotdir':
            r = a2 * (1 if a1 == 'right' else -1)
            r *= -1 if unscramble else 1
            s.rotate(r)
        elif cmd == 'rotpos':
            fr = lambda i0: 1 + i0 + (1 if i0 >= 4 else 0)
            if not unscramble:
                i0 = s.index(a1)
                r = fr(i0)
                s.rotate(r)
            else:
                i1 = s.index(a1)
                i0 = next(i0 for i0 in range(len(s)) if (i0 + fr(i0)) % len(s) == i1)
                s.rotate(i0 - i1)
        elif cmd == 'rev':
            l = list(s)
            sli = slice(a1, a2 + 1)
            l[sli] = reversed(l[sli])
            s = deque(l)
        elif cmd == 'move':
            if unscramble:
                a1, a2 = a2, a1
            c = s[a1]
            del s[a1]
            s.insert(a2, c)

    return ''.join(s)


def main():
    input = open('input').read().strip()
    str_init = 'abcdefgh'
    hash = 'fbgdceah'

    instr = []
    for m in pattern.finditer(input):
        if m['swpos']:
            instr.append(('swpos', int(m['swpos1']), int(m['swpos2'])))
        elif m['swlet']:
            instr.append(('swlet', m['letter1'], m['letter2']))
        elif m['rotdir']:
            instr.append(('rotdir', m['dir'], int(m['nstep'])))
        elif m['rotpos']:
            instr.append(('rotpos', m['letter'], None))
        elif m['rev']:
            instr.append(('rev', int(m['revpos1']), int(m['revpos2'])))
        elif m['move']:
            instr.append(('move', int(m['mvpos1']), int(m['mvpos2'])))

    s1 = scramble(instr, str_init)
    s2 = scramble(instr, hash, unscramble=True)

    print(s1)
    print(s2)


main()
