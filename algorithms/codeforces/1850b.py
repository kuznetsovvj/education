# https://codeforces.com/contest/1850/problem/B

def check(seq):
    mx, midx = -1, 0
    for idx, item in enumerate(seq):
        if item[1] > mx and item[0] <= 10:
            mx, midx = item[1], idx + 1
    return midx

for _ in range(int(input())):
    r = []
    for _ in range(int(input())):
        r.append(tuple(map(int, input().split())))
    print(check(r))