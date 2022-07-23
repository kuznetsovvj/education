# https://codeforces.com/contest/1675/problem/B

def sol():
    n = int(input())
    seq = list(map(int, input().split()))
    cnt = 0
    for i in range(n-2, -1, -1):
        if seq[i+1] == 0:
            return -1
        while seq[i] >= seq[i+1]:
            seq[i] //= 2
            cnt += 1
    return cnt


tt = int(input())
for t in range(tt):
    print(sol())