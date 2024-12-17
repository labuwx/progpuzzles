#!/usr/bin/env python3

from collections import deque


'''
Register A: 61657405
Register B: 0
Register C: 0
Program: 2,4,1,2,7,5,4,3,0,3,1,7,5,5,3,0

2,4  # bst 4
1,2  # bxl 2
7,5  # cdv 5
4,3  # bxc 3
0,3  # adv 3
1,7  # bxl 7
5,5  # out 5
3,0  # jnz 0

bst 4  # RB = cv % 8
bxl 2  # RB ^= v
cdv 5  # RC = RA >> cv
bxc 3  # RB ^= RC
adv 3  # RA = RA >> cv
bxl 7  # RB ^= v
out 5  # OUT cv % 8
jnz 0  # JNZ 0

RB = RA % 8
RB ^= 2
RC = RA >> RB
RB ^= RC
RA = RA >> 3
RB ^= 7
OUT RB % 8
JNZ 0

OUT ((RA % 8) ^ (RA >> ((RA % 8) ^ 2)) ^ 5) % 8
RA = RA >> 3
JNZ 0
'''


def main():
    prog = [2, 4, 1, 2, 7, 5, 4, 3, 0, 3, 1, 7, 5, 5, 3, 0]

    q = [(len(prog), 0)]
    while q:
        k, ra1 = q.pop()

        if k == 0:
            s2 = ra1  # first one is the smallest
            continue

        for ra2 in range(8):
            ra = (ra1 << 3) + ra2

            out = ((ra % 8) ^ (ra >> ((ra % 8) ^ 2)) ^ 5) % 8

            if out == prog[k - 1] and ra != 0:
                q.append((k - 1, ra))

    print(s2)


main()
