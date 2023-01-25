# https://codeforces.com/problemset/problem/466/C


def check(seq):
    # если сумма не делится на 3, то ответ 0
    s = sum(seq)
    if s % 3 != 0:
        return 0
    
    # если сумма элементов [i; len(seq)] равна S/3, то cnt[i] = 1
    # иначе cnt[i] = 0
    cnt = [0 for _ in range(len(seq))]
    sm = 0
    for j in range(len(seq) - 1, -1, -1):
        sm += seq[j]
        if s == sm * 3:
            cnt[j] = 1
    
    # sums[j] = cnt[j] + cnt[j+1] + ... + cnt[n]
    sums = [0 for _ in range(len(seq))]
    sums[-1] = cnt[-1]
    for j in range(len(seq) - 2, -1, -1):
        sums[j] = sums[j+1] + cnt[j]
    
    sm, res = 0, 0
    for i in range(0, len(seq)-2):
        sm += seq[i]
        if sm * 3 == s:
            res += sums[i+2]
    
    return res


input()
seq = tuple(map(int, input().split()))

print(check(seq))

