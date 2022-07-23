# https://codeforces.com/problemset/problem/230/A

s, n = map(int, input().split())
seq = []
for _ in range(n):
    f, b = map(int, input().split())
    seq.append((f, b))
seq.sort(key=lambda x:x[0])

suc = True
if s <= seq[0][0]:
    print('NO')
    suc = False
else:
    s += seq[0][1]
    for i in range(1, len(seq)):
        if s <= seq[i][0]:
            print('NO')
            suc = False
            break
        else:
            s += seq[i][1]

if suc:
    print('YES')