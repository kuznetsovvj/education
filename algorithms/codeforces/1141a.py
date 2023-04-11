# https://codeforces.com/problemset/problem/1141/A

from copy import copy


n, m = map(int, input().split())
s = set()
s.add(n)
t = 0
flag = False
while s:
    if m in s:
        print(t)
        flag = True
        break
    tmp = set()
    for it in s:
        if it * 2 <= m:
            tmp.add(it*2)
        if it * 3 <= m:
            tmp.add(it*3)
    s = tmp
    t += 1

if not flag:
    print(-1)