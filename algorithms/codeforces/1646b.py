# https://codeforces.com/problemset/problem/1646/B

import sys


def solution(seq):
    seq.sort()
    mn = seq[0] + seq[1]
    mx = seq[-1]
    if mn < mx:
        return "YES"
    for k in range((len(seq) - 3) // 2):
        mn += seq[2+k]
        mx += seq[-2-k]
        if mn < mx:
            return "YES"
    return "NO"

input_ = [list(map(int, line.strip().split())) for line in sys.stdin]
for pos in range(2, len(input_), 2):
    print(solution(input_[pos]))