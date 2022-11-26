# https://codeforces.com/problemset/problem/1186/A

a, b, c = map(int, input().split())
if a <= b and a <= c:
    print("Yes")
else:
    print("No")