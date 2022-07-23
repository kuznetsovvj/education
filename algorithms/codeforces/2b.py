# https://codeforces.com/problemset/problem/2/B

import sys

# Определят коэффициент степени при разложении на простые множители
def simple(n, k):
    cnt = 0
    while n and n % k == 0:
        cnt += 1
        n = n // k
    return cnt

def dp(matrix, k):
    # таблица с динамическими коэффициентами
    cf = [[simple(item, k) for item in line] for line in matrix]
    # первая строка и столбец
    for i in range(1, len(matrix)):
        cf[i][0] += cf[i-1][0]
        cf[0][i] += cf[0][i-1]

    for j in range(1, len(matrix)):
        for i in range(1, len(matrix)):
            cf[j][i] += min(cf[j-1][i], cf[j][i-1])
    
    # восстановление ответа
    res = ""
    while i + j > 0:
        if j == 0 or (i != 0 and cf[j][i-1] < cf[j-1][i]):
            res += "R"
            i -= 1
        else:
            res += "D"
            j -= 1
    
    res = res[::-1]
    return cf[-1][-1], res

def solution(matrix):
    
    cnt, res = min(dp(matrix, 2), dp(matrix, 5))
    if cnt > 1:
        for j in range(len(matrix)):
            for i in range(len(matrix)):
                if matrix[j][i] == 0:
                    res = "R" * i + "D" * j + "R" * (len(matrix) - 1 - i) + "D" * (len(matrix) - 1 - j)
                    cnt = 1
                    break
    print(cnt)
    print(res)




input_ = [list(map(int, line.strip().split())) for line in sys.stdin]
solution(input_[1:])