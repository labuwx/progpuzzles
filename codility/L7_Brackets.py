from collections import deque

pmap = {'(': ')', '[': ']', '{': '}'}


def solution(S):
    q = deque()
    for c in S:
        if c in pmap:
            q.append(c)
        elif len(q) == 0 or pmap[q.pop()] != c:
            return 0

    return int(len(q) == 0)
