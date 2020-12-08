#!/usr/bin/env python3


def exec(instr):
    acc, ip = 0, 0
    ins_vis = set()
    while ip < len(instr):
        ins_vis.add(ip)
        cmd, val = instr[ip]
        if cmd == 'acc':
            acc += val
        if cmd == 'jmp':
            ip += val
        else:
            ip += 1
        if ip in ins_vis:
            break
    return acc, ip


inv_cmd = {'nop': 'jmp', 'jmp': 'nop'}


def main():
    input = open('input').read().strip().split('\n')
    instr = [(cmd, int(val)) for l in input for cmd, val in [l.split()]]

    s1 = exec(instr)[0]

    instr2 = list(instr)
    for i in range(len(instr2)):
        cmd, val = instr2[i]
        if cmd not in inv_cmd:
            continue
        instr2[i] = (inv_cmd[cmd], val)
        acc, ip = exec(instr2)
        instr2[i] = (cmd, val)
        if ip == len(instr2):
            s2 = acc
            break

    print(s1)
    print(s2)


main()
