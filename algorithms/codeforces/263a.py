# https://codeforces.com/problemset/problem/263/A

s = []
for _ in range(5):
    s.append(tuple(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if s[i][j]:
            print(abs(i-2) + abs(j-2))
            break
