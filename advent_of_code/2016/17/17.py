#!/usr/bin/env python3

from collections import deque
import hashlib


# 4th quadrant coordinates
direrctions = [((0, -1), 'U'), ((0, 1), 'D'), ((-1, 0), 'L'), ((1, 0), 'R')]


def md5(txt):
    hash = hashlib.new('md5', txt.encode('ascii')).hexdigest().lower()
    return hash


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def get_adj(pos, salt, path):
    room_hash = md5(salt + path)[:4]

    for (dir, c), door in zip(direrctions, room_hash):
        npos = cadd(pos, dir)
        if 0 <= min(npos) and max(npos) <= 3 and door in 'bcdef':
            yield (npos, path + c)


def main():
    input = open('input').read().strip()
    salt = input
    target = (3, 3)

    s1, s2 = None, -1
    q = deque([((0, 0), '')])
    while q:
        pos, path = q.popleft()
        if pos == target:
            s1 = path if s1 == None else s1
            s2 = max(s2, len(path))
            continue
        adj = get_adj(pos, salt, path)
        q.extend(adj)

    print(s1)
    print(s2)


main()
