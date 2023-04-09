# https://codeforces.com/problemset/problem/479/C

i = int(input())
ex = [0] * i
for t in range(i):
    ex[t] = tuple(map(int, input().split()))
ex.sort(key=lambda x:(x[0], x[1]))

current = min(ex[0][0], ex[0][1])
for e in ex[1:]:
    if e[1] >= current:
        current = e[1]
    else:
        current = e[0]

print(current)

