# https://codeforces.com/problemset/problem/1557/A

def check(seq):
    return (sum(seq) - max(seq)) / (len(seq) - 1) + max(seq)


for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))