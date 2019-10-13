def ncr(n, k):
    # return 1
    if n < k:
        return 0
    r = 1
    while n != 0 and r != 0 and k != 0:
        nn, kk = n % 3, k % 3

        if nn < kk:
            bc = 0
        elif nn == kk or kk == 0:
            bc = 1
        else:
            bc = 2

        r *= bc
        n //= 3
        k //= 3
    return r % 3


def triangle(row):
    n = len(row)
    res = 0
    for (k, c) in enumerate(row):
        if c == 'R':
            d = 0
        elif c == 'G':
            d = 1
        else:
            d = 2
        res += ncr(n - 1, k) * d
    res %= 3
    if n % 2 == 0:
        res = (3 - res) % 3
    return 'RGB'[res]
