# https://codeforces.com/problemset/problem/1367/B

def check(seq):
    c, w = 0, 0
    for idx, it in enumerate(seq):
        if it % 2 == 1:
            c += 1
        if idx % 2 != it % 2:
            w += 1
    if len(seq) // 2 != c:
        return -1
    else:
        return w // 2

t = int(input())
for _ in range(t):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))