# https://codeforces.com/contest/1579/problem/C

import sys


def sol(lines, k):
    s = list()
    checked = set()
    for idx_row, line in enumerate(lines):
        for idx_col, item in enumerate(line):
            if item == '*':
                s.append((idx_row, idx_col))
    
    max_col = len(lines[0])
    
    for ast in s[::-1]:
        if ast not in checked and ast[0] < k:
            return 'NO'
        if ast not in checked:
            left = check(ast, lines, checked, max_col, True, 0)
            right = check(ast, lines, checked, max_col, False, 0)

            if not left[1] and not right[1]:
                if left[0] != right[0] or left[0] < k:
                    return "NO"
            
            if not left[1]:
                if left[0] < k:
                    return "NO"
            
            if not right[1]:
                if right[0] < k:
                    return "NO"

    return 'YES'

def check(ast, lines, checked, max_col, left, size):
    if lines[ast[0]][ast[1]] == '*':
        checked.add(ast)
    else:
        return (size, False)
    
    if ast[0] == 0:
        return (size + 1, False)
    
    if left:
        if ast[1] >= 1:
            return check((ast[0]-1, ast[1]-1), lines, checked, max_col, True, size + 1)
        else:
            return (size + 1, True)
    
    if not left:
        if ast[1] < max_col - 1:
            return check((ast[0]-1, ast[1]+1), lines, checked, max_col, False, size + 1)
        else:
            return (size + 1, True)


p = [line.strip() for line in sys.stdin]

i = 1
while i < len(p):
    ll, _, k = map(int, p[i].split())
    lines = []
    for l in range(ll):
        lines.append(p[i + 1 + l])
    print(sol(lines, k))
    i = i + ll + 1

