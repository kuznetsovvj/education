# https://codeforces.com/contest/1547/problem/C

def sol(k, s1, s2):
    res = []
    crt = k
    while s1 and s2:
        if not s1[0]:
            res.append(0)
            del s1[0]
            crt += 1
            continue
        if not s2[0]:
            res.append(0)
            del s2[0]
            crt += 1
            continue
        m = min(s1[0], s2[0])
        if m > crt:
            return -1
        res.append(m)
        if m == s1[0]:
            del s1[0]
            continue
        if m == s2[0]:
            del s2[0]
            continue
    if len(s1) > 0:
        while s1:
            if s1[0] > crt:
                return -1
            if not s1[0]:
                crt += 1
            res.append(s1[0])
            del s1[0]
    if len(s2) > 0:
        while s2:
            if s2[0] > crt:
                return -1
            if not s2[0]:
                crt += 1
            res.append(s2[0])
            del s2[0]
    return " ".join(list(map(str, res)))



t = int(input())
for tt in range(t):
    input()
    k, _, _ = map(int, input().strip().split())
    seq1 = list(map(int, input().strip().split()))
    seq2 = list(map(int, input().strip().split()))
    print(sol(k, seq1, seq2))