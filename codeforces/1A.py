import fileinput
import math

l = fileinput.input()[0][:-1]
ls = l.split(' ')

n = float(ls[0])
m = float(ls[1])
a = float(ls[2])

x = math.ceil(n / a)
y = math.ceil(m / a)

print(int(x * y))
