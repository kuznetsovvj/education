# https://codeforces.com/contest/1810/problem/C

def check(seq, d, c):
    t = len(seq) - len(set(seq))
    seq = sorted(list(set(seq)))
    # все удалим
    res = c + len(seq) * d
    c_accumulate = 0
    for idx, item in enumerate(seq):
        if idx == 0:
            c_accumulate = item - 1
        else:
            c_accumulate += item - seq[idx-1] - 1
        delta = (len(seq) - 1 - idx) * d
        res = min(res, c_accumulate * c + delta)
    if t > 0:
        res += t * d
    return res

for _ in range(int(input())):
    _, c, d = map(int, input().split())
    seq = list(map(int, input().split()))
    print(check(seq, c, d))