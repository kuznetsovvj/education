# https://codeforces.com/problemset/problem/136/A


x = int(input())
seq = tuple(map(int, input().split()))
res = [0 for _ in range(x)]

for idx, item in enumerate(seq):
    res[item-1] = idx+1

print(' '.join(map(str, res)))
