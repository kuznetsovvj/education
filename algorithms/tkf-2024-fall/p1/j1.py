# O(1) - запутался с квадратными уравнениями :(
import math


def check(n, m):
    total = n * m * (n * m + 1) // 2
    diff_min = total
    vertical = True
    k0 = (-2 - 2 * m * (n - 1) + ((2 + 2*m*(n-1))**2 + 8*(m + m*m*n))*0.5) / 4
    k_ceil = math.ceil(k0)
    k_floor = math.floor(k0)

    for k in (k_ceil, k_floor, k_floor - 1, k_ceil + 1):
        # все суммы, это тоже арифметические прогрессии
        s1 = (((1 + k) / 2)  + ((m * (n - 1) + 1) + (m * (n - 1) + k)) / 2) * k * n / 2
        s = abs(s1 - (total - s1))
        if s < diff_min:
            k_min = k + 1 # нумерация с одного
            vertical = True
            diff_min = s

    j0 = (-2 + 2 * (1 + 2*m*n*(m*n + 1))**0.5) / (4*m)
    j_ceil = math.ceil(j0)
    j_floor = math.floor(j0)
    for j in (j_ceil, j_floor, j_ceil + 1, j_floor - 1):
        s1 = m * j * (m * j + 1) // 2
        s = abs(s1 - (total - s1))
        if s < diff_min:
            k_min = j + 1
            vertical = False
            diff_min = s
    if vertical:
        return f"V {k_min}"
    return f"H {k_min}"



for _ in range(int(input())):
    n, m = map(int, input().split())
    print(check(n, m))