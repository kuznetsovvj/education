# https://codeforces.com/problemset/problem/266/B

l, t = map(int, input().split())
line = list(input())
for k in range(t):
    changes = False
    prev = line[0]
    for i in range(1, l):
        if line[i] == 'G' and prev == 'B':
            line[i] = 'B'
            line[i-1] = 'G'
            prev = 'G'
            changes = True
        else:
            prev = line[i]
    if not changes:
        break
print(''.join(map(str, line)))