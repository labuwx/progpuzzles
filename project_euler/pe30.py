def digitsum(n, k):
    dsum = 0

    while n:
        dsum += (n % 10) ** k
        n //= 10
        
    return dsum
    

l = []
n = 10

while n:
    if n == digitsum(n, 5):
        l.append(n)
        print l
        print sum(l)
        print ''
    n += 1
