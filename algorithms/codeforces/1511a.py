# https://codeforces.com/problemset/problem/1511/A

def check(seq):
    res = 0
    for i in seq:
        if i == 1 or i == 3:
            res += 1
    return res

for _ in range(int(input())):
    input()
    print(check(map(int, input().split())))
