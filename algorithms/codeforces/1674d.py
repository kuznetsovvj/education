# https://codeforces.com/contest/1674/problem/D

import sys


def sol(seq):
    if len(seq) % 2 == 0:
        for k in range(2, len(seq), 2):
            if max(seq[k-1], seq[k-2]) > min(seq[k], seq[k+1]):
                return "NO"            
    else:
        if len(seq) == 1:
            return "YES"
        if min(seq[1], seq[2]) < seq[0]:
            return "NO"
        for k in range(3, len(seq), 2):
            if max(seq[k-1], seq[k-2]) > min(seq[k], seq[k+1]):
                return "NO"
    return "YES"       

p = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(p), 2):
    print(sol(p[i]))
