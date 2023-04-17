# https://codeforces.com/problemset/problem/698/A

n = int(input())
vac, spo, con = [float('inf') for _ in range(n)], [float('inf') for _ in range(n)], [float('inf') for _ in range(n)]
seq = tuple(map(int, input().split()))
for idx, item in enumerate(seq):
    if item == 0:
        if idx == 0:
            vac[0] = 1
        else:
            vac[idx] = min([vac[idx-1], spo[idx-1], con[idx-1]]) + 1
    elif item == 1:
        if idx == 0:
            vac[0] = 1
            con[0] = 0
        else:
            vac[idx] = min([vac[idx-1], spo[idx-1], con[idx-1]]) + 1
            con[idx] = min([vac[idx-1], spo[idx-1]])
    elif item == 2:
        if idx == 0:
            vac[0] = 1
            spo[0] = 0
        else:
            vac[idx] = min([vac[idx-1], spo[idx-1], con[idx-1]]) + 1
            spo[idx] = min([vac[idx-1], con[idx-1]])
    else:
        if idx == 0:
            vac[0] = 1
            spo[0] = 0
            con[0] = 0
        else:
            vac[idx] = min([vac[idx-1], spo[idx-1], con[idx-1]]) + 1
            spo[idx] = min([vac[idx-1], con[idx-1]])
            con[idx] = min([vac[idx-1], spo[idx-1]])
print(min(vac[n-1], spo[n-1], con[n-1]))


