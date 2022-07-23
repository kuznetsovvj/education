# https://codeforces.com/contest/1674/problem/E

import math

def sol(seq):
    aim = [math.ceil(i / 2) for i in seq]
    aim.sort()
    m = aim[0] + aim[1]
    res = min(m, check2(seq, 0))
    res = min(res, check2(seq, len(seq) - 2))
    for k in range(0, len(seq) - 2):
        res = min(res, check3(seq, k))
    return res

def check2(seq, i):
    mx = max(seq[i], seq[i+1])
    mn = min(seq[i], seq[i+1])
    
    if mx > 2*mn:
        return math.ceil(mx / 2)
    
    return math.ceil((mx + mn) / 3)

def check3(seq, i):
    if seq[i] == max(seq[i], seq[i+1], seq[i+2]):
        return check2(seq, i+1)
    if seq[i+2] == max(seq[i], seq[i+1], seq[i+2]):
        return check2(seq, i)

    v1 = float('inf')    
    if seq[i+1] >= 2*seq[i] and seq[i+1] >= 2*seq[i+2]:
        v1 = max(seq[i], seq[i+2])
    
    if seq[i+1] > seq[i] and seq[i+1] > seq[i+2]:
        v1 = min(v1, min(seq[i], seq[i+2]) + math.ceil((max(seq[i], seq[i+2]) - min(seq[i], seq[i+2])) / 2))

    else:
        if seq[i] > seq[i+2]:
            return min(v1, check2(seq, i+1))
        else:
            return min(v1, check2(seq, i))
    
    return v1


input()
seq = tuple(map(int, input().strip().split()))
print(sol(seq))


assert check3((5, 2, 5), 0) == 3
assert check2((4, 7), 0) == 4

