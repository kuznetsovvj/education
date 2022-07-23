# https://codeforces.com/problemset/problem/581/A

a, b = map(int, input().split())
print(f"{min(a,b)} {(max(a,b) - min(a,b)) // 2}")