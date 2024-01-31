from collections import defaultdict

d = defaultdict(dict)
_, m, _ = map(int, input().split())
for _ in range(m):
    p1, num, p2 = map(int, input().split())
    d[p1][num] = p2
    d[p2][num] = p1
seq = tuple(map(int, input().split()))

res = True
from_ = 1
for item in seq:
    if item in d[from_]:
        from_ = d[from_][item]
    else:
        res = 0
        break
if not res:
    print(0)
else:
    print(from_)

        

    

