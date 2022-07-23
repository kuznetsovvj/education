# https://codeforces.com/problemset/problem/750/A

n, k = map(int, input().split())
t = 240 - k
i = 0
while i < n:
    i += 1
    t -= 5*i
    if t < 0:
        i -= 1
        break
print(i)