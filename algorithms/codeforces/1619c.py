# https://codeforces.com/contest/1619/problem/C
# Сложность
# Попыток

import sys

def solution(n1, n2):
    i, j = len(n1) - 1, len(n2) - 1
    res = []
    while i > -1 and j > -1:
        if int(n2[j]) < int(n1[i]):
            j -= 1
            z = int(n2[j])*10 + int(n2[j+1])
            if z < 10 or z > 18:
                return -1
            t = z - int(n1[i])
        else:
            t = int(n2[j]) - int(n1[i])
        j -= 1
        i -= 1
        res.append(t)
    if i >= 0:
        return -1
    if j >= 0:
        for k in range(j, -1, -1):
            res.append(n2[k])
    if not res[-1]:
        res.pop()
    
    return ''.join(map(str, res[::-1]))


inp = [line.strip().split() for line in sys.stdin]

for i in range(1, len(inp)):
    print(solution(*inp[i]))
