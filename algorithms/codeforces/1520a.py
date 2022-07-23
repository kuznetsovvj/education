# https://codeforces.com/contest/1520/problem/A

def sol(w):
    s = set()
    prev = ""
    for item in w:
        if item != prev and item in s:
            return 'NO'
        s.add(item)
        prev = item
    return 'YES'

t = int(input())
for tt in range(t):
    input()
    print(sol(input().strip()))