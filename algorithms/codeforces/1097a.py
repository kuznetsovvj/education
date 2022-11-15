# https://codeforces.com/problemset/problem/1097/A

tm = input()
seq = input().split()
fl = False
for i in seq:
    if i[0] == tm[0] or i[1] == tm[1]:
        fl = True
        break
if fl:
    print("YES")
else:
    print("NO")