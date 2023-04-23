# https://codeforces.com/problemset/problem/445/A

def check(m):
    res = []
    for lidx, line in enumerate(m):
        lin = []
        for cidx, item in enumerate(line):
            if item == '-':
                lin.append(item)
            else:
                if (cidx + lidx) % 2 == 0:
                    lin.append('B')
                else:
                    lin.append('W')
        res.append(lin)
    for line in res:
        print(''.join(line))

m = []
n, _ = map(int, input().split())
for _ in range(n):
    m.append(input())
check(m)