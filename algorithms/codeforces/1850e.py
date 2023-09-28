# https://codeforces.com/contest/1850/problem/E

def check(seq, s):
    sm, sq = 0, 0
    for item in seq:
        sm += item
        sq += item**2
    d = 4 * (sm**2) - 4 * len(seq) * (sq - s)
    x1 = (-2 * sm + d**0.5) // (4 * len(seq))
    return int(x1)



for _ in range(int(input())):
    _, s = map(int, input().split())
    seq = tuple(map(int, input().split()))
    print(check(seq, s))