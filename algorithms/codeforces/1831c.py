# https://codeforces.com/contest/1831/problem/C

# наивная идея с проходом и удалением "лишних" ребер - тупиковая, не пролезает по скорости
# из подсказки чумовая идея: dfs + динамика

import sys
from collections import defaultdict
from collections import deque

# старое корявое решение на проходы
def check(v):
    n, d = 1, set([1])
    i = 0
    while len(v) > 0:
        if v[i][0] in d or v[i][1] in d:
            d.add(v[i][0])
            d.add(v[i][1])
            del v[i]
        else:
            i += 1
        if len(v) == 0:
            return n
        if len(v) == i:
            i = 0
            n += 1
    return n

# стильная и модная динамика + dfs
def check2(v):
    dp = [0 for _ in range(len(v)+2)] # номер прохода для каждой из вершин
    idxs = [0 for _ in range(len(v)+2)] # индекс ребра в первоначальном порядке для каждой из вершин
    dp[1] = 1 # номер прохода для первой вершины
    idxs[1] = 0
    vertex = defaultdict(set)
    for idx, item in enumerate(v): # словарь связности для ребер
        vertex[item[0]].add((item[1], idx))
        vertex[item[1]].add((item[0], idx))
    visited = set([1]) # уже посещенные
    queue = [] # рабочая очередь
    for j in vertex[1]:
        queue.append((j,1)) # j - кортеж вершина, номер ребра, 1 - из какой вершины мы пришли
    while len(queue) > 0:
        vp = queue.pop()
        if vp[0][0] in visited:
            continue
        else:
            if idxs[vp[1]] <= vp[0][1]: # если индекс нашего ребра позже родительского - все ок
                dp[vp[0][0]] = dp[vp[1]]
            else:
                dp[vp[0][0]] = dp[vp[1]] + 1
            idxs[vp[0][0]] = vp[0][1]
            visited.add(vp[0][0])
            for j in vertex[vp[0][0]]:
                if j[0] not in visited:
                    queue.append((j, vp[0][0]))
    return max(dp)


inp_ = tuple([line.strip() for line in sys.stdin])
i = 1
t = int(inp_[i])
while i < len(inp_):
    v = list(map(lambda x:tuple(map(int, x.split())), inp_[i+1:i+1+t-1]))
    print(check2(v))
    i += t
    if i >= len(inp_):
        break
    t = int(inp_[i])
