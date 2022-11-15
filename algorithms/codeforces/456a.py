# https://codeforces.com/problemset/problem/456/A

t = int(input())
fl = False
for _ in range(t):
     a, b = map(int, input().split())
     if a != b:
        print("Happy Alex")
        fl = True
        break
if not fl:
    print("Poor Alex")
