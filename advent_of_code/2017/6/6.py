#!/usr/bin/env python3


def next_cfg(mem):
    l = len(mem)
    v = max(mem)
    i = mem.index(v)

    mem_new  = tuple((v + (i-j)%l) // l + (0 if i==j else m) for j, m in enumerate(mem))

    return mem_new


input = open('input').read()
mem = tuple(int(word) for word in input.split('\t'))

cfgs = [mem]
while True:
    mem = next_cfg(mem)
    if mem in cfgs:
        break
    else:
        cfgs.append(mem)

print(len(cfgs))
print(len(cfgs) - cfgs.index(mem))

