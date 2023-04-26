# https://codeforces.com/problemset/problem/1469/A
 
def z(char, vars):
    t = set()
    if char == ')':
        for i in vars:
            if i - 1 >= 0:
                t.add(i-1)
    if char == '(':
        for i in vars:
            t.add(i+1)
    if char == '?':
        for i in vars:
            t.add(i+1)
            if i - 1 >= 0:
                t.add(i-1)
    return t
 
 
def check(w):
    vars = set([0])
    for i in w:
        vars = z(i, vars)
        if len(vars) == 0:
            return "NO"
    if 0 in vars:
        return "YES"
    return "NO"
            
 
for _ in range(int(input())):
    print(check(input()))