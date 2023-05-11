# https://codeforces.com/contest/1829/problem/G

import bisect


def check(n):
    # узнаем, в каком ряду находится значение
    s = bisect.bisect_right(starts, n)
    left, right = n, n
    res = 0
    while s > 1 or (left != starts[s-1] and right != finished[s-1]):
        for i in range(left, right+1):
            res += i**2
        if left != starts[s-1]:
            left = left - s
        else:
            left = left - s + 1
        if right != finished[s-1]:
            right = right - s + 1
        else:
            right = right - s
        s -= 1
    if s >= 1:
        for i in range(1, right+1):
            res += i ** 2
    return res

# предподсчет сумм и границ
st, fn = 1, 1
d = 1
starts = [1]
finished = [1]
sums = [1]
while len(starts) < 2024:
    starts.append(finished[-1]+1)
    finished.append(starts[-1]+d)
    d += 1
    # if len(starts) < 1024:
    #     res = 0
    #     for i in range(starts[-1], finished[-1]+1):
    #         res += i**2
    #     sums.append(sums[-1] + res)


for _ in range(int(input())):
    print(check(int(input())))