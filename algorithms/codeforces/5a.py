# https://codeforces.com/problemset/problem/5/A


import sys


def solution(seq):
    s, res = set(), 0
    for item in seq:
        if item[0] == "+":
            s.add(item[1:])
            continue
        if item[0] == "-":
            s.remove(item[1:])
            continue
        msg = len(item) - item.index(":") - 1
        res += msg * len(s)
    return res

inp = [line.strip() for line in sys.stdin]
print(solution(inp))


