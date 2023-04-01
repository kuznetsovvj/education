# https://codeforces.com/problemset/problem/1196/A

def check(seq):
    return seq[1] + ((seq[2] - (seq[1] - seq[0])) // 2)

for _ in range(int(input())):
    seq = list(map(int, input().split()))
    seq.sort()
    print(check(seq))