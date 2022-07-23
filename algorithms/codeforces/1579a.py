# https://codeforces.com/contest/1579/problem/A

from collections import Counter

def solution(w):
    c = Counter(w)
    if c['B'] == c['A'] + c['C']:
        return "YES"
    return "NO"

t = int(input())
for tt in range(t):
    print(solution(input().strip()))
