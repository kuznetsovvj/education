# https://codeforces.com/problemset/problem/381/A

from collections import deque


input()
seq = tuple(map(int, input().split()))
d = deque(seq)
se, dm = 0, 0
se_ = True
while len(d) > 0:
    if d[0] > d[-1]:
        if se_:
            se += d.popleft()
        else:
            dm += d.popleft()
    else:
        if se_:
            se += d.pop()
        else:
            dm += d.pop()
    se_ = not se_
print(f"{se} {dm}")