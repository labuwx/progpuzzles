#!/usr/bin/env python3

import time
from pphelp import *

m = np.random.randint(1000000000000, size=(20, 20))

start = time.time()
me = mexp(m, 5435354534525455555434343454354543343434352334)
stop = time.time()

print(m)
print(stop - start)



