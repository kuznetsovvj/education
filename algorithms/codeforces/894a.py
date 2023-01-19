# https://codeforces.com/problemset/problem/894/A

s = input()
l, r = [0 for _ in range(len(s))], [0 for _ in range(len(s))]

if s[0] == 'Q':
    l[0] = 1

if s[-1] == 'Q':
    r[-1] = 1


for i in range(1, len(s)):
    if s[i] == 'Q':
        l[i] = l[i-1] + 1
    else:
        l[i] = l[i-1]

for j in range(len(s)-2, -1, -1):
    if s[j] == 'Q':
        r[j] = r[j+1] + 1
    else:
        r[j] = r[j+1]

res = 0
for z in range(len(s)):
    if s[z] == 'A':
        res += l[z] * r[z]

print(res)