# https://codeforces.com/contest/1650/problem/C


import sys


def solution(n, coords):
    coords.sort(key=lambda x:x[1])
    result = coords[:2*n]
    sum_ = sum([k[1] for k in result])
    result.sort(key=lambda x:x[0])
    res_ = []
    for k in range(n):
        res_.append([result[k][2], result[2*n-k-1][2]])
    return (sum_, res_)



input_ = [tuple(map(int, line.strip().split())) for line in sys.stdin]
pos = 2
while True:
    k = 1
    if pos >= len(input_):
        break
    n, m = input_[pos]
    coords = []
    pos += 1
    for z in range(m):
        x, w = input_[pos]
        coords.append((x, w, z + 1))
        pos += 1
    sum_, res_ = solution(n, coords)
    print(sum_)
    for i in res_:
        print(i[0], i[1])
    pos += 1


