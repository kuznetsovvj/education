# https://codeforces.com/contest/1807/problem/B

def check(seq):
    s_a, s_b = 0, 0
    for i in seq:
        if i % 2 == 0:
            s_a += i
        else:
            s_b += i
    if s_a > s_b:
        return "YES"
    return "NO"

for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))