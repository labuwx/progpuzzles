#!/usr/bin/env python3

import re
import numpy as np


input = open('input').read()
input = re.sub(r'[^\d]', '', input)
input = np.array(list(map(int, input)))

mask1 = input == np.roll(input, -1)
s1 = sum(input[mask1])

mask2 = input == np.roll(input, -(len(input) // 2))
s2 = sum(input[mask2])

print(s1)
print(s2)
