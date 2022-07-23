# https://codeforces.com/problemset/problem/1638/A

import sys


def solution(seq):
    pos = 0
    while pos < len(seq) and seq[pos] == pos + 1:
        pos += 1
    # последовательность уже упорядочена
    if pos == len(seq): 
        return ' '.join(map(str, seq))
    end = seq.index(pos + 1)
    tmp = seq[pos:end+1]
    res = seq[:pos] + tmp[::-1] + seq[end+1:]
    return ' '.join(map(str, res))
    

input_ = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(input_), 2):
    print(solution(input_[i]))