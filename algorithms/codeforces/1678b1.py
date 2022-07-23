# https://codeforces.com/problemset/problem/1678/B1

def sol(seq):
    # превратим в последовательность длин
    crt, t = 1, seq[0]
    r = []
    for i in range(1, len(seq)):
        if seq[i] == t:
            crt += 1
        else:
            r.append(crt)
            crt, t = 1, seq[i]
    r.append(crt)

    not_rev = True
    res = 0
    for item in r:
        z = item % 2 == 0
        if (z and not_rev) or (not z and not not_rev):
            not_rev = True
            continue
        res += 1
        not_rev = False
    return res


t = int(input())
for tt in range(t):
    input()
    print(sol(input()))
