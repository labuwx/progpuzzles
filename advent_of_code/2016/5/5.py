#!/usr/bin/env python3

import re
from binascii import hexlify
from hashlib import md5

room = 'wtnhxymk'


passw = ''
i = 0

while len(passw) < 8:
    str2hash = room + str(i)
    hash = hexlify(md5(str2hash.encode('utf8')).digest()).decode('utf8')
    if hash[:5] == '0' * 5:
        passw += hash[5]
        print(passw)
    i += 1
