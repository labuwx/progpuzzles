#!/usr/bin/env python3

from collections import deque


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def add(a, b, n=1):
    return tuple(ai + n * bi for ai, bi in zip(a, b))


def get_tag(mapstr, width, height, node):
    assert mapstr[node] == '.'

    tag_dir = next(
        (d for d in directions if 65 <= ord(mapstr.get(add(node, d), ' ')) <= 90), None
    )
    if tag_dir == None:
        return (None, None)

    tag = ''.join(mapstr.get(add(node, tag_dir, i)) for i in range(1, 3))
    if -1 in tag_dir:
        tag = tag[::-1]

    # type 1=inside, -1=outside
    x, y = node
    if tag in {'AA', 'ZZ'}:
        type = 0
    elif (f := tag_dir[0]) :  # horizontal, x
        type = f * (1 if x < width // 2 else -1)
    else:  # vertical, y
        f = tag_dir[1]
        type = f * (1 if y < height // 2 else -1)

    return (tag, type)


def parse_map(mapstr):
    width, height = max(x for x, _ in mapstr) + 1, max(y for _, y in mapstr) + 1
    graph = {
        pos: get_tag(mapstr, width, height, pos)
        for pos, c in mapstr.items()
        if c == '.'
    }
    return graph


def get_pair(map, node):
    tag = map[node][0]
    assert tag != None
    return next(u for u, (t, _) in map.items() if u != node and t == tag)


def bfs_portal(map, start, end):
    reached = set()
    q = deque([(start, 0)])
    while q:
        pos, dist = q.popleft()
        if pos == end:
            return dist
        if pos in reached:
            continue
        reached.add(pos)
        nbrs = {u for dir in directions if (u := add(pos, dir)) in map}
        if (tag := map[pos])[0] != None and tag[1] != 0:
            nbrs.add(get_pair(map, pos))
        q.extend((u, dist + 1) for u in nbrs)


def bfs_recursive(map, start, end):
    reached = set()
    q = deque([(start, 0, 0)])
    while q:
        pos, dist, level = q.popleft()
        if pos == end and level == 0:
            return dist
        if (pos, level) in reached:
            continue
        reached.add((pos, level))
        q.extend(
            (u, dist + 1, level) for dir in directions if (u := add(pos, dir)) in map
        )
        if (
            (tag := map[pos])[0] != None
            and tag[1] != 0
            and (new_level := level + tag[1]) >= 0
        ):
            q.append((get_pair(map, pos), dist + 1, new_level))


def main():
    input = {
        (x, y): c
        for y, l in enumerate(open('input').read().split('\n'))
        for x, c in enumerate(l)
    }
    map = parse_map(input)

    AA, ZZ = (
        next(u for u, (t, _) in map.items() if t == 'AA'),
        next(u for u, (t, _) in map.items() if t == 'ZZ'),
    )
    s1 = bfs_portal(map, AA, ZZ)
    s2 = bfs_recursive(map, AA, ZZ)

    print(s1)
    print(s2)


main()
