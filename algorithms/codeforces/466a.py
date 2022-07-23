# https://codeforces.com/problemset/problem/466/A

n, m, a, b = map(int, input().split())

# выгоднее разовый или абонемент?
t = b / m
if t >= a:
    # выгоднее разовый
    print(n * a)
else:
    # выгоднее длинный
    k = n // m # количество купленных абонементов
    z = n - (k * m)
    if a * z >= b:
        print((k + 1) * b)
    else:
        print(k * b + a * z)