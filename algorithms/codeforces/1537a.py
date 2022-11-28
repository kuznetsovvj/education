# https://codeforces.com/problemset/problem/1537/A

def check(seq):
    if sum(seq) == len(seq):
        return 0
    if sum(seq) < len(seq):
        return 1
    if sum(seq) > len(seq):
        return sum(seq) - len(seq)

for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))