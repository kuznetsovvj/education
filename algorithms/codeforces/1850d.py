# https://codeforces.com/contest/1850/problem/D

def check(seq, k):
    seq.sort()
    m, c = 1, 1
    for i in range(1, len(seq)):
        if seq[i] - seq[i-1] <= k:
            c += 1
        else:
            m = max(m, c)
            c = 1
    m = max(m, c)
    return len(seq) - m


for _ in range(int(input())):
    _, k = map(int, input().split())
    seq = list(map(int, input().split()))
    print(check(seq, k))