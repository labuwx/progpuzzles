import fileinput
import math
import re

s = " ".join(fileinput.input())
s = re.split(r'\s|\n', s)
s = filter(bool, s)


a1 = int(s[0])
b1 = int(s[1])
a2 = int(s[2])
b2 = int(s[3])
a3 = int(s[4])
b3 = int(s[5])

b = False

b |= (a2 <= a1 and a3 <= a1 and b2 + b3 <= b1) or (
    b2 <= b1 and b3 <= b1 and a2 + a3 <= a1
)

a2, b2 = b2, a2

b |= (a2 <= a1 and a3 <= a1 and b2 + b3 <= b1) or (
    b2 <= b1 and b3 <= b1 and a2 + a3 <= a1
)

a3, b3 = b3, a3

b |= (a2 <= a1 and a3 <= a1 and b2 + b3 <= b1) or (
    b2 <= b1 and b3 <= b1 and a2 + a3 <= a1
)

a2, b2 = b2, a2

b |= (a2 <= a1 and a3 <= a1 and b2 + b3 <= b1) or (
    b2 <= b1 and b3 <= b1 and a2 + a3 <= a1
)

print('YES' if b else 'NO')
