#!/usr/bin/env python3

from bioinf_common import *


s1, s2 = get_dataset().split()
dist = hamm_dist(s1, s2)

print(dist)
