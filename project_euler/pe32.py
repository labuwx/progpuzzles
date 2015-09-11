def digits(n):
    dlist = []

    while n:
        dlist.append(n % 10)
        n //= 10
        
    return dlist

def ispan(a, b, c):
    digitlist = digits(a) + digits(b) + digits(c)
    return (9 == len(digitlist) == len(set(digitlist))) and (0 not in digitlist) 
    
pl = []

for a in range(1, 10 ** 5)  :
    for b in range(a, 10 ** 10):
        if ispan(a, b, a * b):
            pl.append(a*b)

print pl
