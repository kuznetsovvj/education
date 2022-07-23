# https://codeforces.com/problemset/problem/11/A

import math

def sol(seq, d):
    res = 0
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            seq[i] += d
            res += 1
            continue
        if seq[i] < seq[i-1]:
            m = math.ceil((seq[i-1] - seq[i]) / d)
            fl = 0
            if (seq[i-1] - seq[i]) % d == 0:
                fl = 1
            seq[i] += d * (m + fl)
            res += m + fl
    return res

_, d = map(int, input().split())
seq = list(map(int, input().split()))
print(sol(seq, d))
