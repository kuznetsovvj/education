# https://codeforces.com/problemset/problem/339/A

a = list(map(int, input().split('+')))
a.sort()
print('+'.join(map(str, a)))