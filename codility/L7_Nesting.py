def solution(S):
    pc = 0
    for c in S:
        pc += 1 if c == '(' else -1
        if pc < 0:
            return 0

    return int(pc == 0)
