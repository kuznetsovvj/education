# https://codeforces.com/problemset/problem/59/A

a = input()
u, l = 0, 0
for i in range(len(a)):
    if a[i].islower():
        l +=1
    else:
        u += 1
if l >= u:
    print(a.lower())
else:
    print(a.upper())