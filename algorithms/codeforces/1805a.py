# https://codeforces.com/contest/1805/problem/A

def check(seq):
    t = seq[0]
    for i in range(1, len(seq)):
        t = t ^ seq[i]
    if len(seq) % 2 == 0 and t != 0:
        return -1
    if t == 0:
        return 0
    else:
        return t


for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))
