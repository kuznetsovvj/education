# https://adventofcode.com/2023/day/3#part2

def checkaround(m, i, j):
    # left
    res = []
    if j > 0:
        t = j - 1
        if m[i][t].isdigit():
            while t >= 0 and m[i][t].isdigit():
                t -= 1
            res.append(int(m[i][t+1:j]))
    # right
    if j < len(m[i]) - 1:
        t = j + 1
        if m[i][t].isdigit():
            while t < len(m[i]) and m[i][t].isdigit():
                t += 1
            res.append(int(m[i][j+1:t]))
    # up
    if i > 0:
        if m[i-1][j].isdigit():
            st, fn = j, j
            while st >= 0 and m[i-1][st].isdigit():
                st -= 1
            while fn < len(m[i]) and m[i-1][fn].isdigit():
                fn += 1
            res.append(int(m[i-1][st+1:fn]))
        else:
            if j > 0 and m[i-1][j-1].isdigit():
                st, fn = j-1, j-1
                while st >= 0 and m[i-1][st].isdigit():
                    st -=1
                res.append(int(m[i-1][st+1:fn+1]))
            # up-right
            if j < len(m[i]) - 1 and m[i-1][j+1].isdigit():
                st, fn = j+1, j+1
                while fn < len(m[i]) and m[i-1][fn].isdigit():
                    fn += 1
                res.append(int(m[i-1][st:fn]))
    if i < len(m) - 1:
        if m[i+1][j].isdigit():
            st, fn = j, j
            while st >= 0 and m[i+1][st].isdigit():
                st -= 1
            while fn < len(m[i]) and m[i+1][fn].isdigit():
                fn += 1
            res.append(int(m[i+1][st+1:fn]))
        else:
            if j > 0 and m[i+1][j-1].isdigit():
                st, fn = j-1, j-1
                while st >= 0 and m[i+1][st].isdigit():
                    st -=1
                res.append(int(m[i+1][st+1:fn+1]))
            # down-right
            if j < len(m[i]) - 1 and m[i+1][j+1].isdigit():
                st, fn = j+1, j+1
                while fn < len(m[i]) and m[i+1][fn].isdigit():
                    fn += 1
                res.append(int(m[i+1][st:fn]))
    assert len(res) < 3
    if len(res) > 1:
        print(res[0], '*', res[1])
        return res[0] * res[1]
    return 0


def check(m):
    s = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '*':
                s += checkaround(m, i, j)
    return s

assert checkaround(['.......', '...*...', '100.200'], 1, 3) == 20000
assert checkaround(['100*200', '.......', '......'], 0, 3) == 20000
assert checkaround(['.......', '.......', '.......'], 1, 3) == 0
assert checkaround(['.100...', '...*...', '...200.'], 1, 3) == 20000
assert checkaround(['.15*200', '.......', '......'], 0, 3) == 3000
assert checkaround(['100*200', '.......', '......'], 0, 3) == 20000
assert checkaround(['100.200', '...*...', '......'], 1, 3) == 20000

with open(r'C:\edu\algorithms\advent of code 2023\input\03.txt', 'r') as file:
    matrix = []
    for line in file.readlines():
        matrix.append(line.strip())
    
    print(check(matrix))
