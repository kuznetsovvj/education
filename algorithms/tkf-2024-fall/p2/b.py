from collections import deque


n, k = map(int, input().split())
seq = tuple(map(int, input().split()))

d = deque()
for i in range(k):
    while len(d) > 0 and d[-1] > seq[i]:
        d.pop()
    d.append(seq[i])

res = []
res.append(d[0])

for j in range(k, n):
    if len(d) > 0 and d[0] == seq[j - k]:
        d.popleft()
    while len(d) > 0 and d[-1] > seq[j]:
        d.pop()
    d.append(seq[j])
    res.append(d[0])

print(" ".join(map(str, res)))

    

