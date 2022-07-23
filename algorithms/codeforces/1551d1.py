#  https://codeforces.com/contest/1551/problem/D1
#  1700


import sys


def solution(a, b, k):
    # если всю площадь можно разбить на квадраты 2x2
    if a % 2 == 0 and b % 2 == 0:
        if k % 2 == 0 and k >= 0 and k <= a*b // 2:
            return "YES"
        else:
            return "NO"
    # если остается горизонтальная полоса
    if a % 2 == 1:
        if k >= b // 2 and k <= a*b//2 and (k - b//2) % 2 == 0:
            return "YES"
        else:
            return "NO"
    if b % 2 == 1:
        if k >= 0 and k <= a*(b-1)//2 and k % 2 == 0:
            return "YES"
        else:
            return "NO"


inp = [tuple(map(int, line.strip().split())) for line in sys.stdin]

for idx in range(1, len(inp)):
    print(solution(*inp[idx]))
    