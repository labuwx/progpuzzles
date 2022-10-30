def solution(A):
    A = sorted(A)
    M = max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])
    return M
