# https://codeforces.com/problemset/problem/546/A

k, n, w = map(int, input().split())
res = max((w * (w + 1) * k) // 2 - n, 0)
print(res)