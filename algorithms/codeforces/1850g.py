# https://codeforces.com/contest/1850/problem/G

from sys import stdin

input = stdin.readline

# это очень простая задача с точки зрения алгоритма 
# главное побить на категории (вертикаль, горизонталь и два типа диагоналей)
# но оптимизация на питоне потребовала огромного количества сил
# отказ от сохранения в массив входящих данных
# отказ от вызова keys() при проверке ответов
# хранение в словаре ключей в виде строк - почему блять это работает быстрее в 2 раза, чем храние чисел?
for _ in range(int(input())):
    r, c, d1, d2 = {}, {}, {}, {}
    res = 0
    for _ in range(int(input())):
        x1, x2 = map(int, input().split())
        r[str(x1)] = r.get(str(x1), 0) + 1
        c[str(x2)] = c.get(str(x2), 0) + 1
        d1[str(x1+x2)] = d1.get(str(x1+x2), 0) + 1
        d2[str(x1-x2)] = d2.get(str(x1-x2), 0) + 1
    for t in c.values():
        res += t * (t - 1)
    for t in r.values():
        res += t * (t - 1)
    for t in d1.values():
        res += t * (t - 1)
    for t in d2.values():
        res += t * (t - 1)
    print(res)

