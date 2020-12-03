#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass
class Token:
    start: int
    end: int


@dataclass
class Marker(Token):
    length: int
    repeat: int


@dataclass
class CSeq(Token):
    pass


def decompress1(s):
    ns, i = '', 0
    while i < len(s):
        c = s[i]
        if c != '(':
            ns += c
            i += 1
        else:
            ix, icp = s.index('x', i), s.index(')', i)
            l, r = int(s[i + 1 : ix]), int(s[ix + 1 : icp])
            ns += s[icp + 1 : icp + 1 + l] * r
            i = icp + l + 1

    return ns


def dec2_tokenize(s):
    tokens, i = list(), 0
    while i < len(s):
        if s[i] != '(':
            i0 = i
            while i < len(s) and s[i] != '(':
                i += 1
            tokens.append(CSeq(start=i0, end=i - 1))
        else:
            ix, icp = s.index('x', i), s.index(')', i)
            l, r = int(s[i + 1 : ix]), int(s[ix + 1 : icp])
            tokens.append(Marker(start=i, end=icp, length=l, repeat=r))
            i = icp + 1
    return tokens


def dec2_check(tokens):
    isgood = True
    for i1, t1 in enumerate(tokens):
        if not isinstance(t1, Marker):
            continue
        next_token = tokens[i1 + 1]

        cond_next_ischar = isinstance(next_token, CSeq)
        cond_char_only = cond_next_ischar and t1.end + t1.length <= next_token.end
        cond_char_only_if_next_ischar = (not cond_next_ischar) or cond_char_only

        cond_range_end_match = False
        for t2 in tokens[i1 + 1 :]:
            if t1.end + t1.length < t2.start:
                break
            if not isinstance(t2, Marker):
                continue
            cond_crossing = t1.end + t1.length < t2.end + t2.length
            cond_range_end_match = cond_range_end_match or (
                t1.end + t1.length == t2.end + t2.length
            )
            isgood = isgood and not cond_crossing

        isgood = (
            isgood
            and (cond_char_only or cond_range_end_match)
            and cond_char_only_if_next_ischar
        )

    return isgood


def dec2_len(s):
    tokens = dec2_tokenize(s)
    assert dec2_check(tokens)

    declen, i = 0, 0
    while i < len(tokens):
        curr_token, next_token = tokens[i : i + 2]
        if isinstance(curr_token, CSeq):
            declen += curr_token.end - curr_token.start + 1
            i += 1
        elif isinstance(next_token, CSeq):  # curr_token is a Marker
            cseq_len = next_token.end - next_token.start + 1
            declen += cseq_len + curr_token.length * (curr_token.repeat - 1)
            i += 2
        else:  # curr_token is a Marker
            for j in range(i + 1, len(tokens)):
                far_token = tokens[j]
                if curr_token.end + curr_token.length < far_token.start:
                    break
                if not (
                    isinstance(far_token, Marker) and isinstance(tokens[j + 1], CSeq)
                ):
                    continue
                far_token.repeat *= curr_token.repeat
            i += 1

    return declen


def main():
    input = open('input').read().strip()

    s1 = len(decompress1(input))
    s2 = dec2_len(input)

    print(s1)
    print(s2)


main()
