import re


def checkpw(pw):
    lc = dc = 0
    for c in pw:
        if re.match(r'^[a-zA-Z]$', c):
            lc += 1
        elif re.match(r'^[0-9]$', c):
            dc += 1
        else:
            return False
    return (lc % 2) == 0 and (dc % 2) == 1


def solution(S):
    s = max([len(pw) for pw in S.split() if checkpw(pw)] + [-1])
    return s
