# https://codeforces.com/contest/1831/problem/C

# timelimit :()

import sys

def check(v):
    v = list(map(lambda x:tuple(map(int, x.split())), v))
    n, d = 1, set([1])
    i = 0
    while len(v) > 0:
        if v[i][0] in d or v[i][1] in d:
            d.add(v[i][0])
            d.add(v[i][1])
            del v[i]
        else:
            i += 1
        if len(v) == 0:
            return n
        if len(v) == i:
            i = 0
            n += 1
    return n


inp_ = tuple([line.strip() for line in sys.stdin])
i = 1
t = int(inp_[i])
while i < len(inp_):
    print(check(inp_[i+1:i+1+t-1]))
    i += t
    if i >= len(inp_):
        break
    t = int(inp_[i])
