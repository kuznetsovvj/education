# https://codeforces.com/problemset/problem/1631/A

def check(seq1, seq2):
    mx, mn = 0, 0
    for i1, i2 in zip(seq1, seq2):
        cmx = max(i1, i2)
        cmn = min(i1, i2)
        mx = max(cmx, mx)
        mn = max(cmn, mn)
    return mx * mn


for _ in range(int(input())):
    input()
    seq1 = tuple(map(int, input().split()))
    seq2 = tuple(map(int, input().split()))
    print(check(seq1, seq2))