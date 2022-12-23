# https://codeforces.com/problemset/problem/514/A

def check(t):
    n = 1
    res = 0
    while t > 0:
        m = t % 10
        # проверить, что разряд не последний, чтобы не было лидирующих нулей
        if t // 10 > 0:
            if m >= 5:
                res += (9 - m) * n
            else:
                res += m * n
        else:
            if m >= 5 and m < 9:
                res += (9 - m) * n
            else:
                res += m * n
        t = t // 10
        n = n * 10
    return res

print(check(int(input())))