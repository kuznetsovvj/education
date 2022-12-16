# https://codeforces.com/problemset/problem/742/A

# периодичность последний цифры степени

d = {0: 6, 1: 8, 2: 4, 3: 2}
k = int(input())
if k == 0:
    print(1)
else:
    print(d[k % 4])