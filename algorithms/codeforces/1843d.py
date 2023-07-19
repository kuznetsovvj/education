# https://codeforces.com/contest/1843/problem/D

import sys
from collections import defaultdict

def check(vertex, pairs):
    result = [0 for _ in range(len(vertex) + 1)]
    d = defaultdict(set)
    # обработка ребер
    for v in vertex:
        e1, e2 = map(int, v.split())
        d[e1].add(e2)
        d[e2].add(e1)
    # предподсчет ответа для всех вершин
    stack = list()
    stack.append((1, 0))
    while len(stack) > 0:
        # current - что мы сейчас обрабатываем, previous - из какой вершины мы пришли
        current, previous = stack.pop()
        s, r = [], 0
        for v in d[current].difference([previous]):
            if result[v-1] == 0:
                s.append(v)
            else:
                r += result[v-1]
        if len(s) == 0:
            if r == 0:
                result[current-1] = 1
            else:
                result[current-1] = r
        else:
            stack.append((current, previous))
            for i in s:
                stack.append((i, current))
    # выводим ответ
    for pair in pairs:
        p1, p2 = map(int, pair.split())
        print(result[p1-1] * result[p2 - 1])    


inp = tuple(line.strip() for line in sys.stdin)
p = 1
for _ in range(int(inp[0])):
    v = int(inp[p])
    p += 1
    vertex = inp[p:p+v-1]
    p += v - 1
    cmds = int(inp[p])
    p += 1
    pairs = inp[p:p+cmds]
    p += cmds
    check(vertex, pairs)