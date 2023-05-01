# https://codeforces.com/problemset/problem/1792/A

def check(seq):
    c1, c2 = 0, 0
    for i in seq:
        if i <= 1:
            c1 += 1
        else:
            c2 += 1
    return c2 + (c1 // 2) + (c1 % 2)

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))