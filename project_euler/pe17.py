numbers = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}

def digit(n, i):
    k = 10 ** i
    return (n % (10 * k)) // k

def toStr(n):
    s = ''
    
    if n < 100:
        if n in numbers:
            s += numbers[n]
            return s
        a = digit(n, 1)
        if a:
            s += numbers[10 * a]
        n %= 10
    
        a = digit(n, 0)
        if a:
            s += numbers[a]
        
        return s
        
    a = digit(n, 3)
    if a:
        s += numbers[a] + numbers[1000]
    n %= 1000
    
    a = digit(n, 2)
    if a:
        s += numbers[a] + numbers[100]
    n %= 100
    
    if n == 0:
        return s
        
    s += 'and'
    
    if n in numbers:
        s += numbers[n]
        return s
    
    a = digit(n, 1)
    if a:
        s += numbers[10 * a]
    n %= 10
    
    a = digit(n, 0)
    if a:
        s += numbers[a]
        
    return s
    
print sum([len(toStr(n)) for n in range(1, 1001)])
print [toStr(i) for i in range(25)]
print toStr(10)
print toStr(21)
print toStr(12)
print toStr(1000)
print toStr(400)
    