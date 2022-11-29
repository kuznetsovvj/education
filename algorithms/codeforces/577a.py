# https://codeforces.com/problemset/problem/577/A

# Фактически, надо найти количество делителей числа, не привышающих n

n, x = map(int, input().split())

s = set()
for k in range(1, int(x ** 0.5) + 2):
    if x % k == 0 and k <= n and x // k <= n:
        s.add(k)
        s.add(x // k)
print(len(s))