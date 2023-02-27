# https://codeforces.com/problemset/problem/567/A

input()
seq = tuple(map(int, input().split()))
for i in range(len(seq)):
    if i == 0:
        print(seq[1] - seq[0], seq[-1] - seq[0])
        continue
    if i == len(seq) - 1:
        print(seq[-1] - seq[-2], seq[-1] - seq[0])
        continue
    print(min(seq[i+1] - seq[i], seq[i] - seq[i-1]), max(seq[-1] - seq[i], seq[i] - seq[0]))
