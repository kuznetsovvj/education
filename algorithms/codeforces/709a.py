# https://codeforces.com/problemset/problem/709/A

def check(b, d, seq):
    res = 0
    cnt = 0
    for i in seq:
        if i > b:
            continue
        cnt += i
        if cnt > d:
            res += 1
            cnt = 0
    return res

_, b, d = map(int, input().split())
seq = tuple(map(int, input().split()))
print(check(b, d, seq))
