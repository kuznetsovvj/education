# https://codeforces.com/contest/1829/problem/C

def check(seq):
    c1, c2, ct = 10**9, 10**9, 10**9
    for v, item in seq:
        v = int(v)
        if item[0] == '1' and v < c1:
            c1 = v
        if item[1] == '1' and v < c2:
            c2 = v
        if item[0] == '1' and item[1] == '1' and v < ct:
            ct = v
    if (c1 == 10**9 or c2 == 10**9) and ct == 10**9:
        return -1
    else:
        return min(c1 + c2, ct)

for _ in range(int(input())):
    t, res = int(input()), []
    for _ in range(t):
        res.append(tuple(input().split()))
    print(check(res))
