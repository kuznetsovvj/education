# https://codeforces.com/problemset/problem/1729/A

def check(seq):
    t1 = seq[0] - 1
    t2 = abs(seq[1] - seq[2]) + seq[2] - 1
    if t1 == t2:
        return 3
    if t1 < t2:
        return 1
    return 2

for _ in range(int(input())):
    print(check(tuple(map(int, input().split()))))