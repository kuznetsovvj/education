# https://codeforces.com/contest/1744/problem/E1


# неверно...
def check(seq):
    a, b, c, d = seq
    if b <= c and 2*a <= d and a != b:
        return f"{b} {2*a}"
    if 2*a <= c and 2*b <= d:
        return f"{2*a} {2*b}"
    return "-1 -1"
    

t = int(input())
for _ in range(t):
    seq = tuple(map(int, input().split()))
    print(check(seq))