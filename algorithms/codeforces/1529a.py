# https://codeforces.com/problemset/problem/1529/A

def check(seq):
    t, res = min(seq), 0
    for i in seq:
        if i != t:
            res += 1
    return res

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))