# https://codeforces.com/problemset/problem/131/A

a = input()
fl = all([a[i].isupper() for i in range(1, len(a))])
if fl and a[0].isupper():
    print(a.lower())
elif fl and a[0].islower():
    print(a.capitalize())
else:
    print(a)