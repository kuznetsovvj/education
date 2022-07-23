# https://codeforces.com/problemset/problem/282/A

def sol(seq):
    s = 0
    for item in seq:
        if '+' in item:
            s += 1
        else:
            s -= 1
    print(s)

t = int(input())
s = []
for tt in range(t):
    s.append(input())
sol(s)