# https://codeforces.com/contest/1650/problem/D

import sys


def solution(seq):
    step, res = len(seq), []
    while step != 1:
        pos = seq.index(step)
        if pos == step - 1:
            step -= 1
            res.append(0)
            continue
        res.append(pos + 1)
        seq = seq[pos + 1: step] + seq[:pos + 1] + seq[step:]
        step -= 1
    res.append(0)

    return res




input_ = [list(map(int, line.strip().split())) for line in sys.stdin]
for pos in range(2, len(input_), 2):
    print(' '.join(map(str, solution(input_[pos])[::-1])))
