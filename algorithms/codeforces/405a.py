# https://codeforces.com/problemset/problem/405/A

input()
seq = list(map(int, input().split()))
seq.sort()
print(' '.join(map(str, seq)))