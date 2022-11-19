# https://codeforces.com/problemset/problem/1542/A

def check(seq):
    c1 = 0
    for item in seq:
        if item % 2 == 1:
            c1 += 1
    if c1 == len(seq) // 2:
        return "Yes"
    return "No"

for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))
