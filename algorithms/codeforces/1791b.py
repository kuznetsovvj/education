# https://codeforces.com/contest/1791/problem/B

def check(seq):
    x, y = 0, 0
    for c in seq:
        if x == 1 and y == 1:
            return "YES"
        if c == 'L':
            x -= 1
        if c == 'R':
            x += 1
        if c == 'U':
            y += 1
        if c == 'D':
            y -= 1
    if x == 1 and y == 1:
        return "YES"
    return "NO"

for _ in range(int(input())):
    input()
    print(check(input().strip()))