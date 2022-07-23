def sol(m, w):
    res = float('inf')
    for k in range(len(w)):
        for j in range(k+1, len(w)):
            tmp = 0
            if w[k] == w[j]:
                return 0
            for t in range(m):
                tmp += abs(ord(w[k][t]) - ord(w[j][t]))
            res = min(res, tmp)
    return res            

t = int(input().strip())
for tt in range(t):
    n, m = map(int, input().split())
    w = []
    for nn in range(n):
        w.append(input())
    print(sol(m, w))