# https://codeforces.com/problemset/problem/1382/A

def check(seq1, seq2):
    r = seq1.intersection(seq2)
    if len(r) == 0:
        return "NO"
    return f"YES\n1 {r.pop()}"

for _ in range(int(input())):
    input()
    seq1 = set(map(int, input().split()))
    seq2 = set(map(int, input().split()))
    print(check(seq1, seq2))