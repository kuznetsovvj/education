# https://codeforces.com/problemset/problem/1399/A

def check(seq):
    seq = set(seq)
    if max(seq) - min(seq) > len(seq) - 1:
        return 'NO'
    return 'YES'


t = int(input())
for _ in range(t):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))