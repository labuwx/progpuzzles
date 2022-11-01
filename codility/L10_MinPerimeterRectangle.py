import math


def solution(N):
    a = math.ceil(math.sqrt(N))
    while N % a:
        a -= 1
    b = N // a
    return 2 * (a + b)
