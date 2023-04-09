# https://codeforces.com/problemset/problem/1399/C

from collections import defaultdict

# жадное решение, как и ожидалось, не проходит
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

# с подсказкой
# ощущение, что все равно ни хера не понял идею
def check2(seq):
    r = [0] * (len(seq) + 1)
    for item in seq:
        r[item] += 1
    res = 0
    for i in range(2, 2*len(seq) + 1):
        cur = 0
        for t in range(1, (i + 1) // 2):
            if i - t > len(seq):
                continue
            cur += min(r[t], r[i - t])
        if i % 2 == 0:
            cur += r[i // 2] // 2
        res = max(res, cur)
    return res

for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check2(seq))