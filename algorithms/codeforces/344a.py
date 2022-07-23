# https://codeforces.com/problemset/problem/344/A
# Пришлось помучиться с TimeLimit на python

import sys
input = sys.stdin.readline

n = int(input())

res = 0
s = input()
last = s[1]
for i in range(n-1):
    s = input()
    if last == s[0]:
        res += 1
    last = s[1]
    

print(res + 1)