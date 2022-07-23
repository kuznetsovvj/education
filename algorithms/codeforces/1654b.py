# https://codeforces.com/problemset/problem/1654/B

import sys


def solution(w):
    pos = 0  # позиция префикса
    while pos < len(w):
        idx = pos + 1  # позиция поиска повтора
        while idx < len(w) and w[pos] != w[idx]:
            idx += 1
        # не удалось найти ни одного совпадения, выходим
        if idx == len(w):
            break
        # удалось найти совпадение
        while idx < len(w) and pos < len(w) and w[pos] == w[idx]:
            pos += 1
            idx += 1
    return w[pos:]


input_ = [line for line in sys.stdin]
for i in range(1, len(input_)):
    print(solution(input_[i]))