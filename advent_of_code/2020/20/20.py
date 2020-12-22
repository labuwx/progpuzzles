#!/usr/bin/env python3

from collections import defaultdict, deque, Counter
import itertools as it
import numpy as np

# must be in sync with list_edges
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def parse_tile(txt):
    txt = txt.split('\n')
    id = int(txt[0].split()[1][:-1])

    txt = [l for l in txt[1:] if l != '']
    shape = (len(txt[0]), len(txt))
    tile = np.fromfunction(
        np.vectorize(lambda x, y: 1 if txt[y][x] == '#' else 0), shape, dtype=object
    )

    return (id, tile)


def show_tile(t):
    for y in range(t.shape[0]):
        print(''.join('#' if pixel else '.' for pixel in t[:, y]))


def show_edge(e):
    print(''.join('#' if pixel else '.' for pixel in e))


def freeze_edge(edge):
    return tuple(sorted([tuple(edge), tuple(reversed(edge))]))


def inv_orient(orientation):
    rot, mirror = orientation
    new_rot, new_mir = (rot if mirror else -rot) % 4, mirror
    return new_rot, new_mir


def comb_orient(o1, o2):
    rot1, mir1 = o1
    rot2, mir2 = o2
    new_mir = (mir1 + mir2) % 2
    new_rot = (rot1 - rot2) % 4
    return new_rot, new_mir


def orient(tile, orientation):
    rot, mir = orientation
    tile = np.flipud(tile) if mir else tile
    tile = np.rot90(tile, k=rot, axes=(1, 0))
    return tile


# must be in sync with dirs
def list_edges(tile, orientation=None):
    orientation = orientation or (0, 0)
    tile = orient(tile, orientation)

    edges = [tile[0, :], tile[:, -1], tile[-1, ::-1], tile[::-1, 0]]
    return edges


def inner_tile(tile):
    return tile[1:-1, 1:-1]


def main():
    monster = parse_tile(open('monster').read())[1]
    input = open('input').read().strip().split('\n\n')
    tiles = dict(parse_tile(tile) for tile in input)
    shape = next(iter(tiles.values())).shape

    edgemap = defaultdict(set)
    for id, tile in tiles.items():
        for edge in list_edges(tile):
            edgemap[freeze_edge(edge)].add(id)

    adj_cnt = Counter()
    for ids in edgemap.values():
        assert len(ids) <= 2
        if len(ids) == 2:
            for id in ids:
                adj_cnt[id] += 1

    s1 = 1
    for id, n_adj in adj_cnt.items():
        s1 *= id if n_adj == 2 else 1

    q = deque([((0, 0), next(iter(tiles)), 0, 0)])
    posmap = {}
    while q:
        pos, id, rot, mirror = q.popleft()

        if pos in posmap:
            continue
        else:
            posmap[pos] = (id, rot, mirror)

        for i, edge in enumerate(list_edges(tiles[id], (rot, mirror))):
            f_edge = freeze_edge(edge)
            adj_id = next(iter(edgemap[f_edge] - {id}), None)
            if adj_id == None:
                continue

            j, adj_edge = next(
                (j, adj_edge)
                for j, adj_edge in enumerate(list_edges(tiles[adj_id]))
                if freeze_edge(adj_edge) == f_edge
            )

            adj_pos = cadd(pos, dirs[i])
            adj_mir = int((edge == adj_edge).all())
            adj_rot = ((i + 2) - (([2, 1, 0, 3] if adj_mir else [0, 1, 2, 3])[j])) % 4

            q.append((adj_pos, adj_id, adj_rot, adj_mir))

    xmin, ymin, xmax, ymax = *min(posmap), *max(posmap)
    image = np.empty(
        ((xmax - xmin + 1) * (shape[0] - 2), (ymax - ymin + 1) * (shape[1] - 2)),
        dtype=object,
    )
    for (x, y), (id, rot, mirror) in posmap.items():
        itile = inner_tile(orient(tiles[id], (rot, mirror)))
        img_x, img_y = (x - xmin) * (shape[0] - 2), (y - ymin) * (shape[1] - 2)
        image[img_x : (img_x + shape[0] - 2), img_y : (img_y + shape[1] - 2)] = itile

    found = False
    for rot, mirror in it.product(range(4), [0, 1]):
        search_img = orient(image, (rot, mirror))
        monsters = np.zeros_like(search_img)
        for (x, y), _ in np.ndenumerate(search_img):
            x_upper, y_upper = x + monster.shape[0], y + monster.shape[1]
            if x_upper > search_img.shape[0] or y_upper > search_img.shape[1]:
                continue
            search_area = search_img[x:x_upper, y:y_upper]
            if (search_area >= monster).all():
                monsters[x:x_upper, y:y_upper] += monster
                found = True

        if found:
            s2 = (search_img - monsters).sum()
            break

    print(s1)
    print(s2)


main()
