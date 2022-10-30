def solution(A):
    N = len(A)

    lower_ends = sorted(c - r for c, r in enumerate(A))
    upper_ends = sorted(c + r for c, r in enumerate(A))

    s = (N * (N - 1)) // 2
    i = 0
    for le in lower_ends:
        while upper_ends[i] < le:
            i += 1
        s -= i

    return s if s <= 10000000 else -1
