from collections import deque


def solution(H):
    nb = 0
    wall = deque([0])
    for x in H:
        while wall[-1] > x:
            wall.pop()
        if wall[-1] < x:
            nb += 1
            wall.append(x)

    return nb
