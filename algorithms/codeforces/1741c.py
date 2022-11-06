# https://codeforces.com/contest/1741/problem/C

def solution(seq):
    c_m = len(seq)
    for i in range(1, len(seq)):
        if c_m <= i:
            break
        target = sum(seq[:i])
        box, cnt, cnt_max = 0, 0, i
        for k in range(i, len(seq)):
            if box < target:
                box += seq[k]
                cnt += 1
            elif box > target:
                break
            else:
                cnt_max = max(cnt_max, cnt)
                box, cnt = seq[k], 1
        if box == target:
            cnt_max = max(cnt_max, cnt)
            c_m = min(c_m, cnt_max)
    return c_m


for _ in range(int(input())):
    input()
    print(solution(tuple(map(int, input().split()))))