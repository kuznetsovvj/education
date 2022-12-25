# https://codeforces.com/problemset/problem/467/B

def check(k, aim, seq):
    res = 0
    for item in seq:
        r = item ^ aim
        st = str(bin(r))
        s = 0
        for z in st:
            if z == '1':
                s += 1
        if s <= k:
            res += 1
    return res

seq = []
_, m, k = map(int, input().split())
for _ in range(m):
    seq.append(int(input()))
aim = int(input())
print(check(k, aim, seq))