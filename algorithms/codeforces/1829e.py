# https://codeforces.com/contest/1829/problem/E

import sys


# первая версия решения, прошла основные тесты, но упала на взломах по timelimit exceeded
def check(mt):
    useful = [[0 for _ in range(len(mt[0]))] for _ in range(len(mt))]
    smax, scur = 0, 0
    for i in range(len(mt)):
        for j in range(len(mt[0])):
            if not useful[i][j]:
                tmp = set()
                tmp.add((i, j))
                while tmp:
                    x, y = tmp.pop()
                    if mt[x][y] == 0:
                        useful[x][y] = 1
                    else:
                        scur += mt[x][y]
                        useful[x][y] = 1
                        if x != 0 and not useful[x-1][y]:
                            tmp.add((x-1, y))
                        if x != len(mt) - 1 and not useful[x+1][y]:
                            tmp.add((x+1, y))
                        if y != 0 and not useful[x][y-1]:
                            tmp.add((x, y-1))
                        if y != len(mt[0]) - 1 and not useful[x][y+1]:
                            tmp.add((x, y+1))

                smax = max(smax, scur)
                scur = 0
    return smax

# не хочется переписывать все, поправлю аллокации по памяти и сделаю чтение не в input, а через sys.stdin
# помогло
def check2(mt):
    smax, scur = 0, 0
    for i in range(len(mt)):
        for j in range(len(mt[0])):
            if mt[i][j] != -1:
                tmp = set()
                tmp.add((i, j))
                while tmp:
                    x, y = tmp.pop()
                    if mt[x][y] == 0:
                        mt[x][y] = -1
                    else:
                        scur += mt[x][y]
                        mt[x][y] = -1
                        if x != 0 and mt[x-1][y] != -1:
                            tmp.add((x-1, y))
                        if x != len(mt) - 1 and mt[x+1][y] != -1:
                            tmp.add((x+1, y))
                        if y != 0 and mt[x][y-1] != -1:
                            tmp.add((x, y-1))
                        if y != len(mt[0]) - 1 and mt[x][y+1] != -1:
                            tmp.add((x, y+1))

                smax = max(smax, scur)
                scur = 0
    return smax

input_ = tuple(line for line in sys.stdin)
n = int(input_[0])
t, i = 1, 1
while t <= n:
    r, _ = map(int, input_[i].split())
    i += 1
    res = []
    for _ in range(r):
        res.append(list(map(int, input_[i].split())))
        i += 1
    print(check2(res))
    t += 1