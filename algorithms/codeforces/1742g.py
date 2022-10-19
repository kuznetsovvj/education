# https://codeforces.com/contest/1742/problem/G

def check(seq):
    # флаг, что число из последовательности уже было использовано
    used = [False for _ in range(len(seq))]
    steps = min(31, len(seq))
    crt = 0
    res = []
    # количество регистров ограничено (31), поэтому достаточно выбрать 31 самое подходящее число
    for i in range(steps):
        mx, mx_idx = 0, -1
        for idx, item in enumerate(seq):
            if used[idx]:
                continue
            if crt | item > mx:
                mx = crt | item
                mx_idx = idx
        used[mx_idx] = True
        res.append(seq[mx_idx])
        crt = crt | seq[mx_idx]
    for idx, item in enumerate(seq):
        if not used[idx]:
            res.append(item)
    return res

t = int(input())
for _ in range(t):
    input()
    seq = tuple(map(int, input().split()))
    res = check(seq)
    print(' '.join(map(str, res)))
