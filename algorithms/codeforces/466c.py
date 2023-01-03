# https://codeforces.com/problemset/problem/466/C

input()
seq = tuple(map(int, input().split()))

if sum(seq) % 3 != 0:
    print(0)

