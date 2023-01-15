# https://codeforces.com/problemset/problem/1490/A

def check(seq):
    res = 0
    for i in range(1, len(seq)):
        mx = max(seq[i], seq[i-1])
        mn = min(seq[i], seq[i-1])
        if mx / mn <= 2:
            continue
        # наверное, можно более эффективно посчитать через логарифм
        while mx > mn:
            mn = mn * 2
            res += 1
        res -= 1
    return res

for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))