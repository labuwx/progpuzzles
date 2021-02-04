from random import shuffle


def sort_inner(l, mi, ma):
    if mi >= ma:
        return
    p = l[ma]

    i = mi - 1
    for j in range(mi, ma + 1):
        if l[j] > p:
            continue
        i += 1
        l[i], l[j] = l[j], l[i]

    sort_inner(l, mi, i - 1)
    sort_inner(l, i + 1, ma)


def sort(l):
    l = list(l)
    if l:
        shuffle(l)
        sort_inner(l, 0, len(l) - 1)
    return l
