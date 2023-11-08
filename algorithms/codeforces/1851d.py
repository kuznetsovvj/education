# https://codeforces.com/contest/1851/problem/D

def check(k, seq):
    a = set([i for i in range(1, k+1)])
    seq.sort()
    out = []
    if seq[0] in a:
        a.remove(seq[0])
    else:
        out.append(seq[0])
    for i in range(1, len(seq)):
        if seq[i] - seq[i-1] in a:
            a.remove(seq[i] - seq[i-1])
        else:
            out.append(seq[i] - seq[i-1])
    
    if len(out) == 0 or (len(out) == 1 and sum(a) == sum(out)):
        return "YES"
    return "NO"

for _ in range(int(input())):
    k = int(input())
    seq = list(map(int, input().split()))
    print(check(k, seq))