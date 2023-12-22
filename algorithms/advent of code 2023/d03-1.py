# https://adventofcode.com/2023/day/3

def checkaround(m, i, start, finish):
    s = set()
    for t in range(start - 1, finish + 2):
        if t >= 0 and t < len(matrix):
            if i - 1 >= 0:
                s.add(m[i-1][t])
            if i + 1 < len(matrix):
                s.add(m[i+1][t])
    if start - 1 >= 0:
        s.add(m[i][start-1])
    if finish + 1 < len(matrix):
        s.add(m[i][finish+1])
    
    s.remove('.')
    if len(s) >= 1:
        return int(m[i][start:finish+1])
    return 0

def check(m):
    s = 0
    flag = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if m[i][j].isdigit():
                if flag:
                    current += 1
                else:
                    flag = True
                    start = j
                    current = j
            else:
                if flag:
                    s += checkaround(matrix, i, start, current)
                    flag = False
        if flag:
            s += checkaround(matrix, i, start, current)
            flag = False
    return s

with open(r'C:\edu\algorithms\advent of code 2023\input\03.txt', 'r') as file:
    matrix = []
    for line in file.readlines():
        matrix.append(line.strip())
    
    print(check(matrix))
    

    