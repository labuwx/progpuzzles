def solution(A):
    A = sorted(A)
    prev = None
    cnt = 0
    for x in A:
        if x != prev:
            cnt += 1
            prev = x
    return cnt
