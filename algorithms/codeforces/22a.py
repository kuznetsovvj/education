# https://codeforces.com/problemset/problem/22/A

def sol(seq):
    seq = list(set(seq))
    seq.sort()
    if len(seq) > 1:
        return seq[1]
    return "NO"


input()
print(sol(list(map(int, input().split()))))