def solution(N, S, T):
    ql = N // 2
    s = 0

    ul_s = ur_s = bl_s = br_s = ql**2
    for seat in (S + " " + T).split():
        y = int(seat[:-1]) - 1
        x = ord(seat[-1]) - ord('A')
        pos = (x < ql, y < ql)

        if pos == (True, True):
            ul_s -= 1
        elif pos == (False, True):
            ur_s -= 1
        elif pos == (True, False):
            bl_s -= 1
        else:  # (False, False)
            br_s -= 1

    ul_d = ur_d = bl_d = br_d = 0
    for seat in T.split():
        y = int(seat[:-1]) - 1
        x = ord(seat[-1]) - ord('A')
        pos = (x < ql, y < ql)

        if pos == (True, True):
            ul_d += 1
        elif pos == (False, True):
            ur_d += 1
        elif pos == (True, False):
            bl_d += 1
        else:  # (False, False)
            br_d += 1

    if (dd := br_d - ul_d) > 0:
        if ul_s < dd:
            return -1
        else:
            s += dd
            ul_s -= dd
    elif (dd := ul_d - br_d) > 0:
        if br_s < dd:
            return -1
        else:
            s += dd
            br_s -= dd

    if (dd := bl_d - ur_d) > 0:
        if ur_s < dd:
            return -1
        else:
            s += dd
            ur_s -= dd
    elif (dd := ur_d - bl_d) > 0:
        if bl_s < dd:
            return -1
        else:
            s += dd
            bl_s -= dd

    s += (min(ul_s, br_s) + min(ur_s, bl_s)) * 2
    return s
