# https://codeforces.com/problemset/problem/368/B

import sys


def check(seq, cmds):
    s = set()
    k = [0 for _ in range(len(seq))]
    for i in range(len(seq)-1, -1, -1):
        s.add(seq[i])
        k[i] = len(s)
    
    for cmd in cmds:
        print(k[cmd-1])

r = tuple(line for line in sys.stdin)
seq = tuple(map(int, r[1].split()))
cmds = tuple(map(int, r[2:]))
check(seq, cmds)