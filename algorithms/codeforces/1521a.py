# https://codeforces.com/problemset/problem/1521/A

def check(a, b):
    if b == 1:
        print('NO')
        return

    print('YES')
    # a * (b - 1) + a = a * b
    # первые два слагаемые точно кратны а, но не кратны b, т.е. "почти хорошие"
    # сумма кратна a * b - "хорошая"

    # [!] забыл про условие, что все числа различные
    # не работает, если b = 2, тогда a + a = a*b
    print(f'{a * (b + 1)} {a * (b - 1)} {a * b * 2}')


for _ in range(int(input())):
    check(*map(int, input().split()))