while b != c + 17:
    f = 1
    d = 2
    while d != b:
        e = 2
        while e != b:
            if d * e == b:
                f = 0
            e += 1
        d += 1
    if f == 0:
        h += 1
    b += 17
