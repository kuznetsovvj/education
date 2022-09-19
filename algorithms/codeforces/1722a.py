# https://codeforces.com/contest/1722/problem/A

from collections import defaultdict


t = int(input())

for _ in range(t):
    d = defaultdict(int)
    d.update([('T', 1), ('i', 1), ('m', 1), ('u', 1), ('r', 1)])
    input()
    name = input()

    if len(name) != 5:
        print("NO")
        continue

    for i in name:
        d[i] -= 1
        if d[i] < 0:
            print("NO")
            break
    else:
        print("YES")