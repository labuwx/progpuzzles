from collections import deque

DOWNSTRM = 1
UPSTRM = 0


def solution(A, B):
    q = deque()
    for fish in zip(A, B):
        q.append(fish)
        while len(q) >= 2 and q[-2][1] == DOWNSTRM and q[-1][1] == UPSTRM:
            if q[-2][0] > q[-1][0]:
                q.pop()
            else:
                q.rotate(1)
                q.pop()
                q.rotate(-1)

    return len(q)
