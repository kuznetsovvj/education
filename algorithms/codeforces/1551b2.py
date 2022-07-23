#  https://codeforces.com/contest/1551/problem/B2
#  сложность 1400

from collections import defaultdict
import sys

def solution(seq, k):
    # надо считать общее количество вхождений для каждого элемента
    # и номера позиций-вхождений
    cnt = defaultdict(int)
    idxs = defaultdict(list)
    res = {i: set() for i in range(k)}
    res_min = {i: 0 for i in range(k)}
    for idx, item in enumerate(seq):
        cnt[item] += 1
        idxs[item].append(idx)
    # расставим по местам
    i = 0
    for key, value in sorted(cnt.items(), key=lambda item:item[1], reverse=True):
        for z in range(min(value, k)):
            res[i].add(idxs[key][z])
            res_min[i] += 1
            i += 1
            if i > k - 1:
                i = 0
    
    min_ = min(res_min.values())
    result = [0 for _ in range(len(seq))]
    for key, value in res.items():
        while len(value) > min_:
            value.pop()
        for item in value:
            result[item] = key + 1
    
    return result

inp = [tuple(map(int, line.strip().split())) for line in sys.stdin]

for idx in range(1, len(inp), 2):
    _, k = inp[idx]
    seq = inp[idx+1]
    print(' '.join(map(str, solution(seq, k))))