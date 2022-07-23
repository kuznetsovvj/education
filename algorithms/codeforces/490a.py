# https://codeforces.com/problemset/problem/490/A

d = {1:set(), 2:set(), 3:set()}
input()
seq = tuple(map(int, input().split()))
for idx, it in enumerate(seq):
    d[it].add(idx+1)
m = min((len(d[1]), len(d[2]), len(d[3])))
print(m)
for _ in range(m):
    print(f"{d[1].pop()} {d[2].pop()} {d[3].pop()}")