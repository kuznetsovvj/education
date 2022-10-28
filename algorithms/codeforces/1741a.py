# https://codeforces.com/contest/1741/problem/A

def check(a, b):
    if a[-1] == 'S':
        if b[-1] != 'S':
            return '<'
        if len(a) == len(b):
            return "="
        if len(a) == 1:
            return ">"
        if len(b) == 1:
            return "<"
        if len(a) > len(b):
            return "<"
        return ">"
    
    if a[-1] == 'M':
        if b[-1] == 'S':
            return ">"
        if b[-1] == 'L':
            return "<"
        return "="
    
    if a[-1] == 'L':
        if b[-1] != 'L':
            return ">"
        if len(a) == len(b):
            return "="
        if len(a) == 1:
            return "<"
        if len(b) == 1:
            return ">"
        if len(a) > len(b):
            return ">"
        return "<"

t = int(input())
for _ in range(t):
    a, b = input().split()
    print(check(a, b))