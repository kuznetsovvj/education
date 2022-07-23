# https://codeforces.com/problemset/problem/520/A

s = {chr(i) for i in range(ord('a'), ord('z')+1)}
input()
w = input().lower()
for i in range(len(w)):
    if w[i] in s:
        s.remove(w[i])
if len(s) > 0:
    print('NO')
else:
    print('YES')