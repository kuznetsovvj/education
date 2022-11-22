# https://codeforces.com/problemset/problem/279/B

# Классические два указателя

def check(seq, th):
    mx, sm, cnt = 0, 0, 0
    l, r = 0, 0
    while r < len(seq) and l < len(seq):
        while r < len(seq) and th >= sm + seq[r]:
            sm += seq[r]
            cnt += 1
            r += 1
        mx = max(cnt, mx)
        sm -= seq[l]
        cnt -= 1
        l += 1
    return mx

_, th = map(int, input().split())
seq = tuple(map(int, input().split()))
print(check(seq, th))
