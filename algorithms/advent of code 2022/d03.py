# https://adventofcode.com/2022/day/2


line = r'input\03.txt'

with open(line, 'r') as file:
    
    cnt = 0
    for line in file.readlines():
        w = line.strip()
        s = set(w[:len(w) // 2]).intersection(set(w[len(w) // 2:]))
        t = s.pop()
        if t.islower():
            cnt += ord(t) - 96
        else:
            cnt += ord(t) - 38
    
    print("Task A:", cnt)
        