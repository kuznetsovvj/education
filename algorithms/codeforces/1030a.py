# https://codeforces.com/problemset/problem/1030/A

input()
seq = tuple(map(int, input().split()))
if sum(seq) == 0:
    print('EASY')
else:
    print('HARD')