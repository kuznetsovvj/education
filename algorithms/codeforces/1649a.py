# https://codeforces.com/problemset/problem/1649/A


import sys


def solution(seq):
    first, last = -1, -1
    for idx, item in enumerate(seq):
        if not item:
            first = idx - 1
            break
    if first == -1:
        return 0
    for idx in range(len(seq)-1, -1, -1):
        if not seq[idx]:
            last = idx + 1
            break
    return last - first


input_ = [list(map(int, line.strip().split())) for line in sys.stdin]
for pos in range(2, len(input_), 2):
    print(solution(input_[pos]))