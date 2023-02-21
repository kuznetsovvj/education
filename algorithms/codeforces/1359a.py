# https://codeforces.com/problemset/problem/1359/A

def check(n, m , k):
    t = n // k # количество карт у одного человека
    mx = min(t, m) # максимальное количество джокеров на руках у одного человека
    dt = m - mx # сколько осталось неиспользованных
    if dt <= 0:
        return mx # если джокеров хватило только одному - он и победитель
    r = dt // (k - 1) + (dt % (k - 1) != 0) # минимальное количество джокеров, которое может быть у проигравшего
    return mx - r
    

for _ in range(int(input())):
    print(check(*map(int, input().split())))