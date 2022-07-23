# https://codeforces.com/problemset/problem/1399/B

def check(seq1, seq2):
    m1 = min(seq1)
    m2 = min(seq2)
    res = 0
    for i in range(len(seq1)):
        d1, d2 = seq1[i] - m1, seq2[i] - m2
        res += max(d1, d2)
    return res

t = int(input())
for _ in range(t):
    input()
    seq1 = tuple(map(int, input().split()))
    seq2 = tuple(map(int, input().split()))
    print(check(seq1, seq2))