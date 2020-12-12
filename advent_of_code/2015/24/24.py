#!/usr/bin/env python3


def balance(packages, ngroup):
    sp = sum(packages)
    assert sp % ngroup == 0
    group_weight = sp // ngroup

    mem = [(0, 1)] + [None] * group_weight
    for x in packages:
        for w in range(group_weight, 0, -1):
            if w >= x and mem[w - x] != None:
                with_w_count = mem[w - x][0] + 1
                with_w_entag = mem[w - x][1] * x
                if mem[w] == None:
                    mem[w] = (with_w_count, with_w_entag)
                else:
                    if with_w_count < mem[w][0]:
                        mem[w] = (with_w_count, with_w_entag)
                    elif with_w_count == mem[w][0]:
                        mem[w] = (mem[w][0], min(mem[w][1], with_w_entag))

    return mem[-1]


def main():
    input = [int(x) for x in open('input').read().split()]
    # input = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

    s1 = balance(input, 3)[1]
    s2 = balance(input, 4)[1]

    print(s1)
    print(s2)


main()
