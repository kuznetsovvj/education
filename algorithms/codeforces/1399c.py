# https://codeforces.com/problemset/problem/1399/C

from collections import defaultdict


def check(seq):

    if len(seq) == 1:
        return 0

    d = defaultdict(int)
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            w = seq[i] + seq[j]
            d[w] += 1
    
    t = max(d, key=d.get)
    
    res = 0
    flag = [0 for _ in range(len(seq))]
    for i in range(len(seq)):
        if flag[i] == True:
            continue
        for j in range(i+1, len(seq)):
            if seq[i] + seq[j] == t and not flag[j]:
                flag[i] = True
                flag[j] = True
                res += 1
                break
    return res


for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))