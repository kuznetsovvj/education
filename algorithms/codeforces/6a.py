# https://codeforces.com/problemset/problem/6/A

seq = list(map(int, input().strip().split()))
seq.sort()

if seq[0] + seq[1] > seq[2] or seq[1] + seq[2] > seq[3]:
    print("TRIANGLE")

elif seq[0] + seq[1] == seq[2] or seq[1] + seq[2] == seq[3]:
    print("SEGMENT")

else:
    print("IMPOSSIBLE")


