# https://codeforces.com/contest/1714/problem/G

from collections import defaultdict
from bisect import bisect_right

# рекурсивное решение верное, но на больших сетах не проходит по глубине рекурсии
def solution(graph, cnt_v):
    # результаты
    current_value = 0
    result = [0 for i in range(cnt_v + 1)]
    current_line = []
    step(graph, 1, current_value, current_line, result)
    return result[2:]

def step(graph, p, current_value, current_line, result):
    for vertex in graph[p]:
        current_value += vertex[1]
        if len(current_line) >= 1:
            current_line.append(current_line[-1] + vertex[2])
        else:
            current_line.append(vertex[2])
        result[vertex[0]] = bisect_right(current_line, current_value)
        step(graph, vertex[0], current_value, current_line, result)
        current_value -= vertex[1]
        del current_line[-1]

# решение на стеке, без рекурсии
def solution1(graph, cnt_v):
    current_value = 0
    result = [0 for i in range(cnt_v + 1)]
    current_line = []
    stack = []
    for ver in graph[1]:
        stack.append((False, ver[0], ver[1], ver[2]))
        stack.append((True, ver[0], ver[1], ver[2]))
    while stack:
        cmd = stack.pop()
        if cmd[0]:
            current_value += cmd[2]
            if len(current_line) >= 1:
                current_line.append(current_line[-1] + cmd[3])
            else:
                current_line.append(cmd[3])
            result[cmd[1]] = bisect_right(current_line, current_value)
            for vert in graph[cmd[1]]:
                stack.append((False, vert[0], vert[1], vert[2]))
                stack.append((True, vert[0], vert[1], vert[2]))
        else:
            current_value -= cmd[2]
            del current_line[-1]
    return result[2:]

t = int(input())
for _ in range(t):
    # количество вершин
    cnt_v = int(input())
    graph = defaultdict(list)
    for i in range(cnt_v - 1):
        p, a, b = map(int, input().split())
        # i + 2 - фактический номер вершины
        graph[p].append((i + 2, a, b))
    result = ' '.join(map(str, solution1(graph, cnt_v)))
    print(result)
