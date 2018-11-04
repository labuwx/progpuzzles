#!/usr/bin/env python3

from bioinf_common import *


def merge(A, B):
    la, lb = len(A), len(B)
    C, i, j = [], 0, 0
    while True:
        if i < la and j < lb:
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        elif i < la:
            C.append(A[i])
            i += 1
        elif j < lb:
            C.append(B[j])
            j += 1
        else:
            break
    return C


ds = get_dataset().split('\n')
A = [int(x) for x in ds[1].split()]
B = [int(x) for x in ds[3].split()]

C = merge(A, B)
print(*C)
