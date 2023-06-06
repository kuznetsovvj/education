# https://codeforces.com/contest/1838/problem/0

def check(seq):
    mn = min(seq)
    mx = max(seq)
    if mn < 0:
        return mn
    else:
        return mx

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))
