# https://codeforces.com/problemset/problem/703/A

s = 0
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a > b:
        s += 1
    elif a < b:
        s -= 1
if s > 0:
    print('Mishka')
elif s == 0:
    print('Friendship is magic!^^')
else:
    print('Chris')