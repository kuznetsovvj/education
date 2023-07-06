# https://codeforces.com/contest/1836/problem/A

def check(seq):
    d = {}
    for i in seq:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    prev = -1
    prev_value = float('inf')
    for k in sorted(d.keys()):
        if k != prev + 1 or d[k] > prev_value:
            return "NO"
        prev = k
        prev_value = d[k]
    return "YES"


for _ in range(int(input())):
    input()
    print(check(map(int, input().split())))