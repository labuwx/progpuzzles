#!/usr/bin/env python3

import json
import re


def visit(data, ignore_red=False):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(visit(ds, ignore_red) for ds in data)
    elif isinstance(data, dict):
        if ignore_red and 'red' in data.values():
            return 0
        else:
            return sum(visit(ds, ignore_red) for ds in data.values())
    elif isinstance(data, str):
        return 0
    else:
        assert False


def main():
    input = open('input').read().strip()
    input_data = json.loads(input)

    s1 = sum(int(m.group(0)) for m in re.finditer(r'-?\d+', input))
    assert s1 == visit(input_data, ignore_red=False)

    s2 = visit(input_data, ignore_red=True)

    print(s1)
    print(s2)


main()
