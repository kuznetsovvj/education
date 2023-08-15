# https://codeforces.com/contest/1846/problem/C

import sys


def check(pls, time):
    res = [r(pl, time) for pl in pls]
    if len(res) == 1:
        return 1
    ans = 1
    for item in res[1:]:
        if item[1] > res[0][1] or (item[1] == res[0][1] and item[0] < res[0][0]):
            ans += 1
    return ans


def r(pl, time):
    pl.sort()
    i = 0 
    c_time, c_penalty = 0, 0
    while i < len(pl) and c_time <= time:
        if c_time + pl[i] <= time:
            c_time += pl[i]
            c_penalty += c_time
            i += 1
        else:
            break
    return (c_penalty, i)


i = [list(map(int, line.split())) for line in sys.stdin]
row = 1
for _ in range(i[0][0]):
    ps, _, time = i[row]
    row += 1
    players = i[row:row+ps]
    row += ps
    print(check(players, time))