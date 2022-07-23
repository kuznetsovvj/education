# https://codeforces.com/contest/1538/problem/A

import sys


def solution(items):
    max_pos = items.index(max(items))
    min_pos = items.index(min(items))
    l = [max_pos + 1, min_pos + 1]
    r = [len(items) - max_pos, len(items) - min_pos]
    if min(min(l), min(r)) == min(l):
        if min(l) == max_pos + 1:
            return max_pos + 1 + min(min_pos - max_pos, len(items) - min_pos)
        else:
            return min_pos + 1 + min(max_pos - min_pos, len(items) - max_pos)
    else:
        if min(r) == len(items) - max_pos:
            return len(items) - max_pos + min(max_pos - min_pos, min_pos + 1)
        else:
            return len(items) - min_pos + min(min_pos - max_pos, max_pos + 1)



assert solution(list(map(int, "1 5 4 3 2".split()))) == 2
assert solution(list(map(int, "2 1 3 4 5 6 8 7".split()))) == 4
assert solution(list(map(int, "4 2 3 1 8 6 7 5".split()))) == 5
assert solution(list(map(int, "3 4 2 1".split()))) == 3
assert solution(list(map(int, "2 3 1 4".split()))) == 2
assert solution(list(map(int, "1 4 5 3 2".split()))) == 3
assert solution(list(map(int, "2 4 5 3 1".split()))) == 3

input_ = list([tuple(map(int, line.strip().split())) for line in sys.stdin])
for j in range(2, len(input_), 2):
    print(solution(input_[j]))

