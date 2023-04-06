# https://codeforces.com/contest/1805/problem/C

import sys
import bisect


def check(pars, lines):
    for p in pars:
        a, b, c = p
        i = bisect.bisect_left(lines, b)
        for t in range(i-1, i+1):
            if 0 <= t < len(lines) and (b - lines[t])**2 < 4*a*c:
                print("YES")
                print(lines[t])
                break
        else:
            print("NO")


input_ = tuple(line for line in sys.stdin)
z = 1
while z < len(input_):
    l, p = map(int, input_[z].split())
    lines = [0] * l
    par = [0] * p
    z += 1
    for i in range(l):
        lines[i] = int(input_[z])
        z += 1
    lines.sort()
    for i in range(p):
        par[i] = tuple(map(int, input_[z].split()))
        z += 1
    check(par, lines)
        
