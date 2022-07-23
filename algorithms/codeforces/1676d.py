def sol(n, m, w):
    d1, d2 = [0 for i in range(n+m+1)], [0 for i in range(n+m+1)]
    for k in range(n):
        for j in range(m):
            d1[k+j] += w[k][j]
            d2[k-j+m] += w[k][j]
    mx = 0
    for k in range(n):
        for j in range(m):
            mx = max(mx, d1[k+j] + d2[k-j+m] - w[k][j])
    return mx                                            
          

t = int(input().strip())
for tt in range(t):
    n, m = map(int, input().split())
    w = []
    for nn in range(n):
        w.append(tuple(map(int, input().split())))
    print(sol(n, m, w))