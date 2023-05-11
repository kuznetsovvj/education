# https://codeforces.com/contest/1829/problem/B

def check(seq):
    m, c = 0, 0
    for item in seq:
        if not item:
            c += 1
        else:
            m, c = max(m, c), 0
    m = max(m, c)
    return m

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))