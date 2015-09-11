from math import factorial as fact

def iscur(n):
    k = n
    s = 0
    
    while k:
        s += fact(k % 10)
        k //= 10
        
    return n == s
    
n = 10
s = 0

while n:
    if iscur(n):
        print n
        s += n
        print s
        print ''
        
    n += 1
