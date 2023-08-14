# https://codeforces.com/contest/1846/problem/B

def check(s):
    for i in range(3):
        if s[0][i] == s[1][i] == s[2][i] and s[0][i] != '.': 
            return s[0][i]
    for j in range(3):
        if s[j][0] == s[j][1] == s[j][2] and s[j][0] != '.': 
            return s[j][0]
    if s[0][0] == s[1][1] == s[2][2] and s[1][1] != '.':
        return s[0][0]
    if s[0][2] == s[1][1] == s[2][0] and s[1][1] != '.':
        return s[1][1]
    return "DRAW"

for _ in range(int(input())):
    seq = []
    seq.append(input().strip())
    seq.append(input().strip())
    seq.append(input().strip())
    print(check(seq))