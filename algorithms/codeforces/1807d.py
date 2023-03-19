# https://codeforces.com/contest/1807/problem/D

def check(seq, req):
    z = sum(seq)
    pref = [0 for _ in range(len(seq) + 1)]
    pref[0] = 0
    for i in range(len(seq)):
        pref[i+1] = pref[i] + seq[i]
    for reqs in req:
        if (pref[reqs[1]] - pref[reqs[0]-1]) % 2 == reqs[2] * (reqs[1] - reqs[0] + 1) % 2:
            if z % 2 == 1:
                print("YES")
            else:
                print("NO")
        else:
            if z % 2 == 1:
                print("NO")
            else:
                print("YES")

for _ in range(int(input())):
    _, q = map(int, input().split())
    seq = tuple(map(int, input().split()))
    res = []
    for _ in range(q):
        res.append(tuple(map(int, input().split())))
    check(seq, res)
