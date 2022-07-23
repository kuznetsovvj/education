# https://codeforces.com/problemset/problem/3/C
# Сложность 1800
# Количество попыток 3 (потерял два граничных случая)

def solution(lines):
    xc, oc, dc = 0, 0, 0
    for i in range(3):
        for j in range(3):
            if lines[i][j] == "X":
                xc += 1
            if lines[i][j] == "0":
                oc += 1
            if lines[i][j] == ".":
                dc += 1

    if xc != oc and xc != oc + 1:
        return "illegal"
    
    ch = set()
    for i in range(3):
        if lines[0][i] == lines[1][i] == lines[2][i]:
            ch.add(lines[0][i])
    
    for i in range(3):
        if lines[i][0] == lines[i][1] == lines[i][2]:
            ch.add(lines[i][0])
    
    if lines[0][0] == lines[1][1] == lines[2][2]:
        ch.add(lines[1][1])
    
    if lines[0][2] == lines[1][1] == lines[2][0]:
        ch.add(lines[1][1])
    
    if 'X' in ch and '0' in ch:
        return "illegal"
    
    if 'X' in ch and xc == oc + 1:
        return "the first player won"
    
    if 'X' in ch:
        return "illegal"
    
    if '0' in ch and oc == xc:
        return "the second player won"
    
    if '0' in ch and oc < xc:
        return "illegal"
    
    if dc == 0:
        return "draw"

    if xc == oc:
        return "first"
    
    if xc == oc + 1:
        return "second"


lines = [input(), input(), input()]
print(solution(lines))