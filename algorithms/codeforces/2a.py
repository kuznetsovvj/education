# https://codeforces.com/problemset/problem/2/A

import sys
from collections import defaultdict

def solution(scores):
    crt = defaultdict(int)
    mx = defaultdict(list)
    for i in range(1, len(scores)):
        name, score = scores[i][0], int(scores[i][1])
        crt[name] += score
        # первая запись
        if len(mx[name]) == 0:
            mx[name].append((score, i))
        # запись о максимуме
        else:
            if mx[name][-1][0] < crt[name]:
                mx[name].append((crt[name], i))
    
    max_value, names = float('-inf'), []
    for key, value in crt.items():
        if value > max_value:
            names.clear()
            names.append(key)
            max_value = value
            continue
        if value == max_value:
            names.append(key)

    if len(names) == 1:
        return names[0]
    
    min_idx, res = float('inf'), ""
    for name in names:
        for (scores, i) in mx[name]:
            if scores >= max_value:
                if i < min_idx:
                    res = name
                    min_idx = i
                break
    return res

inp = [line.strip().split() for line in sys.stdin]
print(solution(inp))