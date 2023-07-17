# https://codeforces.com/contest/1843/problem/A

def check(seq):
    l, r = 0, len(seq) - 1
    res = 0
    seq.sort()
    while l < r:
        res += seq[r] - seq[l]
        r -= 1
        l += 1
    return res
    

for _ in range(int(input())):
    input()
    print(check(list(map(int, input().split()))))