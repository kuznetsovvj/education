# https://codeforces.com/problemset/problem/110/A

s = input()
res = 0
for i in range(len(s)):
    if s[i] == '7' or s[i] == '4':
        res += 1
res = str(res)
flag = True
for i in range(len(res)):
    if res[i] != '7' and res[i] != '4':
        flag = False
if flag:
    print("YES")
else:
    print("NO")