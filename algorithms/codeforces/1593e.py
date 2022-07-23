# https://codeforces.com/contest/1593/problem/E

from collections import defaultdict

def sol(k, graph):
    compl = set()

    for (key, v) in graph.items():
        if not v or len(v) == 1:
            compl.add(key)

    for i in range(k):
        # удалять уже нечего
        if not compl:
            break
        
        # осталось две вершины, удалим обе
        if len(graph) <= 2:
            graph = dict()
            break
        
        next_step = set()
        for ver in compl:
            v = graph[ver].pop()
            graph[v].remove(ver)
            del graph[ver]
            if len(graph[v]) == 1:
                next_step.add(v)
        compl = next_step
    
    return len(graph)

t = int(input())

for tt in range(t):
    input()
    n, k = tuple(map(int, input().split()))
    d = defaultdict(set)
    for z in range(n-1):
        v1, v2 = tuple(map(int, input().split()))
        d[v1].add(v2)
        d[v2].add(v1)
    print(sol(k, d))
