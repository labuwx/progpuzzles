def merge(l, mi, mid, ma):
    a, b = mi, mid + 1
    l1, inv = [], 0
    for _ in range(mi, ma + 1):
        if b > ma or (a <= mid and l[a] <= l[b]):
            l1.append(l[a])
            a += 1
        elif a > mid or (b <= ma and l[b] < l[a]):
            l1.append(l[b])
            b += 1
            inv += mid + 1 - a
    l[mi : ma + 1] = l1
    return inv


def sort_inner(l, mi, ma):
    if mi == ma:
        return 0
    mid = mi + (ma - mi) // 2
    inv = sort_inner(l, mi, mid) + sort_inner(l, mid + 1, ma) + merge(l, mi, mid, ma)
    return inv


def sort(l, report_inv=False):
    l0 = list(l)
    if l0:
        inv = sort_inner(l0, 0, len(l0) - 1)
    else:
        inv = 0
    return (l0, inv) if report_inv else l0
