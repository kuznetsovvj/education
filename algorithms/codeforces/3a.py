# https://codeforces.com/problemset/problem/3/A

s = input()
t = input()
s1, s2 = ord(s[0]), int(s[1])
t1, t2 = ord(t[0]), int(t[1])
dif1, dif2 = s1 - t1, s2 - t2
res = []
cnt = max(abs(dif1), abs(dif2))

while abs(dif1) > 0 and abs(dif2) > 0:
    res.append("")
    if dif1 < 0:
        res[-1] += "R"
        dif1 += 1
    else:
        res[-1] += "L"
        dif1 -= 1
    if dif2 < 0:
        res[-1] += "U"
        dif2 += 1
    else:
        res[-1] += "D"
        dif2 -= 1

if dif1 > 0:
    for i in range(dif1):
        res.append("L")

if dif1 < 0:
    for i in range(abs(dif1)):
        res.append("R")

if dif2 < 0:
    for i in range(abs(dif2)):
        res.append("U")

if dif2 > 0:
    for i in range(dif2):
        res.append("D")

print(cnt)
for item in res:
    print(item)