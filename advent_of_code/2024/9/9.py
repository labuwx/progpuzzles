#!/usr/bin/env python3


ID, SIZE, PREV, NEXT = 0, 1, 2, 3


def ins_before(x, xx):
    xp = x[PREV]
    x[PREV] = xx
    xx[NEXT] = x
    xx[PREV] = xp
    if xp is not None:
        xp[NEXT] = xx


def rem(x):
    xp = x[PREV]
    xn = x[NEXT]
    if xp is not None:
        xp[NEXT] = xn
    if xn is not None:
        xn[PREV] = xp

    x[PREV] = None
    x[NEXT] = None
    return x


def ecopy(x):
    xx = list(x)
    xx[PREV] = xx[NEXT] = None
    return xx


def lcopy(x):
    M = []
    while x:
        M.append(ecopy(x))
        x = x[NEXT]

    for i in range(len(M) - 1):
        x, y = M[i : i + 2]
        x[NEXT] = y
        y[PREV] = x

    return M[0]


def find_head(x):
    while (prev := x[PREV]) is not None:
        x = prev
    return x


def find_tail(x):
    while (next := x[NEXT]) is not None:
        x = next
    return x


def print_disk(f):
    disk = ''
    while f:
        fid = f[ID]
        disk += (str(fid) if fid is not None else '.') * f[SIZE]
        f = f[NEXT]

    print(disk)


def checksum_1(disk):
    return sum(f * i for i, f in enumerate(disk) if f is not None)


def checksum_2(f):
    cs, idx = 0, 0

    while f:
        if (fid := f[ID]) is not None:
            cs += fid * (2 * idx + f[SIZE] - 1) * f[SIZE] // 2
        idx += f[SIZE]

        f = f[NEXT]

    return cs


def compact_1(disk):
    disk = list(disk)

    i, j = 0, len(disk) - 1
    while i < j:
        if disk[i] is not None:
            i += 1
        elif disk[j] is None:
            j -= 1
        else:
            disk[i], disk[j] = disk[j], None

    return disk


def compact_2(disk):
    disk = lcopy(disk)
    head = disk
    tail = find_tail(disk)
    ftp = tail

    for fid in range(tail[ID], -1, -1):
        while ftp[ID] != fid:
            ftp = ftp[PREV]

        sp = head
        found = False
        while not found and sp != ftp:
            if sp[ID] is None and (sdiff := sp[SIZE] - ftp[SIZE]) >= 0:

                ins_before(sp, ecopy(ftp))
                ftp[ID] = None

                if sdiff:
                    sp[SIZE] = sdiff
                else:
                    rem(sp)

                if ftp[PREV] is not None and ftp[PREV][ID] is None:
                    ftp[SIZE] += ftp[PREV][SIZE]
                    rem(ftp[PREV])

                if ftp[NEXT] is not None and ftp[NEXT][ID] is None:
                    ftp[SIZE] += ftp[NEXT][SIZE]
                    rem(ftp[NEXT])

                found = True

            else:
                sp = sp[NEXT]

    return head


def main():
    input = open('input').read()
    # input = open('input_test').read()

    disk, diskl = [], []
    for k, size in enumerate(input.strip()):
        id = None if k % 2 else k // 2
        size = int(size)

        disk += [id] * size

        x = [id, size, None, None]
        if diskl:
            diskl[-1][NEXT] = x
            x[PREV] = diskl[-1]
        diskl.append(x)
    diskl = diskl[0]

    s1 = checksum_1(compact_1(disk))
    s2 = checksum_2(compact_2(diskl))

    print(s1)
    print(s2)


main()
