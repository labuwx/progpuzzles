#!/usr/bin/env python3

import re
from binascii import hexlify
from hashlib import md5

room = 'wtnhxymk'


passw = ''
passw2 = ['_'] * 8
i = 0

while len(passw) < 8 or passw2.count('_') > 0:
    str2hash = room + str(i)
    hash = hexlify(md5(str2hash.encode('utf8')).digest()).decode('utf8')
    if hash[:5] == '0' * 5:
        if len(passw) < 8:
            passw += hash[5]
            print(passw)
        if hash[5] in '01234567':
            k = int(hash[5])
            if passw2[k] == '_':
                passw2[k] = hash[6]
                print(''.join(passw2))
        print()
    i += 1
