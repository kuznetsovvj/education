# https://codeforces.com/problemset/problem/456/A

input()
seq1 = tuple(map(int, input().split()))
seq2 = tuple(map(int, input().split()))
res = [(seq1[i], seq2[i]) for i in range(len(seq1))]
res.sort(key=lambda x:x[0])
fl = False
for i in range(1, len(seq1)):
    if res[i][1] < res[i-1][1] and res[i][0] > res[i-1][0]:
        fl = True
        break
if fl:
    print("Happy Alex")
else:
    print("Poor Alex")