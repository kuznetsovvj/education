# https://codeforces.com/problemset/problem/25/A

input()
seq = list(map(int, input().split()))
for i in range(len(seq)):
    seq[i] = seq[i] % 2

if sum(seq) == 1:
    print(seq.index(1) + 1)
else:
    print(seq.index(0) + 1)