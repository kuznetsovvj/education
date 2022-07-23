# https://codeforces.com/contest/1538/problem/C
 
import sys
 
 
def solution(l, r, items):
    items.sort()
    res = 0
    down, up = len(items) - 1, len(items) - 1
    k = 0
    while k < len(items) - 1:
        upflag, downflag = False, False
        while items[k] + items[up] > r and up > k + 1:
            up -= 1
        if items[k] + items[up] <= r:
            upflag = True
        down_j = k + 1
        while items[k] + items[down_j] < l and down_j < down:
            down_j += 1
        if items[k] + items[down_j] >= l:
            downflag = True
        k += 1
        if not downflag:
            continue
        if not upflag:
            return res
        res += up - down_j + 1
        down = min(down_j + 1, len(items) - 1)
    return res
 
assert(solution(4, 7, [5, 1, 2])) == 2
assert(solution(5, 8, [5, 1, 2, 4, 3])) == 7
assert(solution(100, 1000, [1, 1, 1, 1])) == 0
assert(solution(9, 13, [2, 5, 5, 1, 1])) == 1
 
"""
input_ = [tuple(map(int, line.strip().split())) for line in sys.stdin]
for j in range(1, len(input_), 2):
    _, l, r = input_[j]
    items = input_[j+1]
    print(solution(l, r, items))
"""
