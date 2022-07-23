# https://codeforces.com/problemset/problem/12/A
# Попыток: 1
# Сложность: 800

import sys

def solution(lines):
    for i in range(3):
        for j in range(3):
            if lines[i][j] == 'X': 
                if lines[2-i][2-j] != 'X':
                    return "NO"
    return "YES"

inp = [line.strip() for line in sys.stdin]
print(solution(inp))