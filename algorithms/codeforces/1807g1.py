# https://codeforces.com/contest/1807/problem/G1

# неверное решение во время контеста
def check(seq):
    if len(seq) == 1:
        if seq[0] == 1:
            return "YES"
        return "NO"

    t = max(seq)
    idx_t = seq.index(t)
    seq = seq[:idx_t] + seq[idx_t+1:]
    l, r = 0, 0
    current = seq[0]
    while current != t:
        if current < t:
            if r == len(seq) - 1:
                return "NO"
            r += 1
            current += seq[r]
            continue
        if current > t:
            current -= seq[l]
            l += 1
    if current == t:
        return check(seq)
    
# решение с подсказки
def check2(seq):
    seq.sort()
    if seq[0] != 1:
        return "NO"
    sm = 1
    for i in range(1, len(seq)):
        if seq[i] > sm:
            return "NO"
        else:
            sm += seq[i]
    return "YES"

for _ in range(int(input())):
    input()
    seq = list(map(int, input().split()))
    print(check2(seq))