# https://codeforces.com/problemset/problem/1692/A

def check(seq):
    cnt = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[0]:
            cnt += 1
    return cnt

for _ in range(int(input())):
    print(check(tuple(map(int, input().split()))))