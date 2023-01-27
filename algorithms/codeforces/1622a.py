# https://codeforces.com/problemset/problem/1622/A


# говнокод
def check(seq):
    seq.sort()
    s = set(seq)
    if len(s) == 3:
        if seq[0] + seq[1] == seq[2]:
            return "YES"
        return "NO"
    if len(s) == 1:
        if s.pop() % 2 == 0:
            return "YES"
        return "NO"
    if seq[0] == seq[1]:
        if seq[2] % 2 == 0:
            return "YES"
        return "NO"
    if seq[1] == seq[2]:
        if seq[0] % 2 == 0:
            return "YES"
        return "NO"


for _ in range(int(input())):
    seq = list(map(int, input().split()))
    print(check(seq))