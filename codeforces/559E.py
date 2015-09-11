import fileinput
import re

si = " ".join(fileinput.input())
si = re.split(r'\s|\n', si)
si = map(int, filter(bool, si))

n = si[0]
ll = zip(si[1::2], si[2::2])
ll.sort()

dmap = {}
def maxl(k, ultmp):
    ul = tuple(sorted(ultmp))
    if (k, ul) in dmap:
        return dmap[(k, ul)]

    if k == 0:
        val = 0
    else:
        lc = ll[k-1]
        v1 = maxl(k-1, ul + ((lc[0] - lc[1], lc[0]),) )
        v2 = maxl(k-1, ul + ((lc[0], lc[0] + lc[1]),) )
        val = max(v1, v2)
    
    dmap[(k, ul)] = val
    return val

print n
print ll
print ''
print maxl(n, ())
