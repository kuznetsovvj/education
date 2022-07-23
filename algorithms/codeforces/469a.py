# https://codeforces.com/problemset/problem/469/A

n = int(input())
seq1 = tuple(map(int, input().split()))
seq2 = tuple(map(int, input().split()))
r = set(seq1[1:]).union(set(seq2[1:]))

fl = True
for i in range(1, n+1):
    if i not in r:
        fl = False
        break
if fl:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")