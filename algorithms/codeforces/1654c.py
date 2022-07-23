# https://codeforces.com/problemset/problem/1654/C

import sys
import bisect


def solution(seq):
    seq.sort()
    ans = [sum(seq)]
    while len(seq) > 0:
        if seq[-1] > ans[-1]:
            return "NO"
        if seq[-1] == ans[-1]:
            seq.pop()
            ans.pop()
            continue
        t = ans.pop()
        if t % 2 == 0:
            idx = bisect.bisect_right(ans, t // 2)
            ans = ans[:idx] + [t // 2, t // 2] + ans[idx:]
        else:
            idx = bisect.bisect_right(ans, t // 2)
            ans = ans[:idx] + [t // 2, t // 2 + 1] + ans[idx:]
    if len(seq) == 0:
        return "YES"
    return "NO"


input_ = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(input_), 2):
    print(solution(input_[i]))