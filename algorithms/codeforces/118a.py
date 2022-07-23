# https://codeforces.com/problemset/problem/118/A

d = {'a', 'o', 'y', 'e', 'u', 'i'}

a = input().lower()
r = ""
for item in a:
    if item in d:
        continue
    r += f".{item}"
print(r)