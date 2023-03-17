# https://codeforces.com/problemset/problem/766/B

def check(seq):
    seq.sort()

    for i in range(2, len(seq)):
        if seq[i-2] + seq[i-1] > seq[i]:
            return "YES"
    return "NO"

input()
seq = list(map(int, input().split()))
print(check(seq))