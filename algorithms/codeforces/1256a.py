# https://codeforces.com/problemset/problem/1256/A

def check(a, b, n, S):
    # a, b - количество
    # n - номинал монеты
    # S - сумма

    # максимальное количество, сколько можно взять монет большого номинала
    a_max = S // n
    a_real = min(a_max, a)
    d_S = S - a_real * n
    if b < d_S:
        return "NO"
    return "YES"

for _ in range(int(input())):
    print(check(*map(int, input().split())))