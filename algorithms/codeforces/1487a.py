# https://codeforces.com/problemset/problem/1487/A

def check(seq):
    m = min(seq)
    res = 0
    for i in seq:
        if i != m:
            res += 1
    return res

for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))