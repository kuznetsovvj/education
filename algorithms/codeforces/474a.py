# https://codeforces.com/problemset/problem/474/A

line = "qwertyuiopasdfghjkl;zxcvbnm,./"

m = input()
l = input()

if m == 'R':
    k = -1
else:
    k = 1

res = []
for item in l:
    res.append(line[line.index(item) + k])
print(''.join(res))
