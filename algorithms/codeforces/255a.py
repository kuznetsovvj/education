# https://codeforces.com/problemset/problem/255/A

input()
seq = tuple(map(int, input().split()))
ch, bi, ba = 0, 0, 0
for i in range(len(seq)):
    if i % 3 == 0:
        ch += seq[i]
    if i % 3 == 1:
        bi += seq[i]
    if i % 3 == 2:
        ba += seq[i]

t = max([ch, bi, ba]) 
if t == ch:
    print("chest")
elif t == bi:
    print("biceps") 
else:
    print("back")