# https://codeforces.com/contest/1810/problem/0

def check(seq):
    for idx, item in enumerate(seq):
        if item <= idx + 1:
            return "YES"
    return "NO"


for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))