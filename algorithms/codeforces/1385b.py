# https://codeforces.com/problemset/problem/1385/B

def check(seq):
    res, s = [], set()
    for it in seq:
        if it not in s:
            res.append(it)
            s.add(it)
    return ' '.join(map(str, res))

t = int(input())
for _ in range(t):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))