# https://codeforces.com/problemset/problem/158/B

from collections import Counter


input()
seq = tuple(map(int, input().split()))
c = Counter(seq)
# все группы по 4
res = c[4]
# все группы по 3
res += c[3]
# к троечникам подсадим группы из 1
c[1] = max(0, c[1] - c[3])

res += c[2] // 2
# не уместившаяся пара
if c[2] % 2 == 1:
    c[1] += 2

res += c[1] // 4
if c[1] % 4 != 0:
    res += 1

print(res)