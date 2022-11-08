# https://codeforces.com/contest/1722/problem/D

def check(seq):
    dt, cnt = [], 0
    for i in range(len(seq)):
        if seq[i] == 'L':
            cnt += i
            dt.append(max(len(seq) - 1 - i, i) - i)
        else:
            cnt += len(seq) - 1 - i
            dt.append(max(len(seq) - 1 - i, i) - (len(seq) - 1 - i))
    dt.sort(reverse=True)
    
    for i in range(1, len(dt)):
        dt[i] += dt[i-1]
    
    for i in range(len(dt)):
        dt[i] += cnt
    
    return dt


for _ in range(int(input())):
    input()
    seq = input()
    print(' '.join(map(str, check(seq))))