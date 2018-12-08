#!/usr/bin/env python3


def parse_tree(l_ext):
    l = list(reversed(l_ext))
    tree, idc = {}, 0
    def parse_tree_inner(parent):
        nonlocal idc
        id = idc
        idc += 1
        num_child = l.pop()
        num_attr = l.pop()
        children = [parse_tree_inner(id) for _ in range(num_child)]
        attributes = [l.pop() for _ in range(num_attr)]
        tree[id] = {
            'parent': parent,
            'attributes': attributes,
            'children': children
        }
        return id
    parse_tree_inner(None)
    return tree


def checksum2(tree, node_id):
    node = tree[node_id]
    chldrn = node['children']
    cs = 0
    for attr in node['attributes']:
        if len(chldrn) == 0:
            cs += attr
        elif attr - 1 in range(len(chldrn)):
            cs += checksum2(tree, chldrn[attr-1])
    return cs


input = [int(x) for x in open('input').read().split()]
tree = parse_tree(input)

s1 = sum(attr for node in tree.values() for attr in node['attributes'])
s2 = checksum2(tree, 0)

print(s1)
print(s2)
