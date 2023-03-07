# https://codeforces.com/problemset/problem/1472/C

def check(seq):
    res = [0 for _ in range(len(seq))]
    for i in range(len(seq)):
        if res[i] == 0:
            res[i] = seq[i]

        # если следующий "прыжок" выгоден
        if i + 1 + seq[i] <= len(seq):
            res[i + seq[i]] = max(res[i + seq[i]], seq[i + seq[i]] + res[i])
    return max(res)

for _ in range(int(input())):
    input()
    seq = list(map(int, input().split()))
    print(check(seq))