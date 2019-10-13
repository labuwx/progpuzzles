#!/usr/bin/env python3


def digits(n):
    dgs = []
    while n:
        dgs.append(n % 10)
        n //= 10
    if not dgs:
        dgs = [0]
    return list(reversed(dgs))


def kmp_prec(seq):
    j, failure_array = 0, [0]
    for c in seq[1:]:
        while j > 0 and seq[j] != c:
            j = failure_array[j - 1]
        if seq[j] == c:
            j += 1
        failure_array.append(j)
    return failure_array


def kmp_adv(pat, prec, c, j):
    while j > 0 and pat[j] != c:
        j = prec[j - 1]
    if pat[j] == c:
        j += 1
    return j


input = int(open('input').read().strip())
init = [3, 7]

recipes = list(init)
ep1, ep2 = 0, 1
while len(recipes) < input + 10:
    sc1, sc2 = recipes[ep1], recipes[ep2]
    sm = sc1 + sc2
    recipes.extend(digits(sm))
    ep1 = (ep1 + 1 + sc1) % len(recipes)
    ep2 = (ep2 + 1 + sc2) % len(recipes)
s1 = ''.join(str(x) for x in recipes[input : input + 10])

recipes = list(init)
sq = digits(input)
ep1, ep2 = 0, 1
prec, j, fnd = kmp_prec(sq), 0, False
for d in recipes:
    j = kmp_adv(sq, prec, d, j)
while not fnd:
    sc1, sc2 = recipes[ep1], recipes[ep2]
    sm = sc1 + sc2
    for d in digits(sm):
        recipes.append(d)
        j = kmp_adv(sq, prec, d, j)
        if j == len(sq):
            fnd = True
            break
    ep1 = (ep1 + 1 + sc1) % len(recipes)
    ep2 = (ep2 + 1 + sc2) % len(recipes)
s2 = len(recipes) - len(sq)

print(s1)
print(s2)
