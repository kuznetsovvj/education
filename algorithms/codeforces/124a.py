# https://codeforces.com/problemset/problem/124/A

n, a, b = map(int, input().split())
res = n - max(a + 1, n - b) + 1
print(res)