# https://codeforces.com/contest/1744/problem/C

def check(seq, n):
    if n == 'g':
        return 0
    wait = False
    cnt, max_cnt = 0, float('-inf')
    for t in seq:
        if wait:
            cnt += 1
            if t == 'g':
                max_cnt = max(cnt, max_cnt)
                wait = False
        else:
            if t == n:
                wait = True
                cnt = 0
    if wait:
        i = 0
        cnt += 1
        while seq[i] != 'g':
            i += 1
            cnt += 1
        max_cnt = max(cnt, max_cnt)
    return max_cnt


t = int(input())
for _ in range(t):
    _, n = input().split()
    seq = input()
    print(check(seq, n))