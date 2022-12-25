# https://codeforces.com/problemset/problem/1760/A

for _ in range(int(input())):
    seq = list(map(int, input().split()))
    seq.sort()
    print(seq[1])