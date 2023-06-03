# https://codeforces.com/contest/1839/problem/B

import sys
from collections import deque


def check(seq):
    seq.sort(key=lambda x:x[1], reverse=True)
    seq.sort(key=lambda x:x[0])
    res, crt, threshold = 0, 0, 0
    s = deque()
    for item in seq:
        if item[0] > threshold:
            s.append(item[0])
            res += item[1]
            crt += 1
            threshold = max(crt, threshold)
            t = s.popleft()
            while len(s) != 0 and t <= threshold:
                t = s.popleft()
            if t > threshold:
                s.appendleft(t)
            crt = len(s)
        else:
            continue
    return res


inp = [line.strip() for line in sys.stdin]
i = 1
for _ in range(int(inp[0])):
    t = int(inp[i])
    i += 1
    print(check(list(map(lambda x:tuple(map(int, x.split())), inp[i:i+t]))))
    i += t
