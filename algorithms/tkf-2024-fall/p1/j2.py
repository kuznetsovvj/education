# бинпоиск вместо перебора

def check(n, m):
    # разрез по вертикали, перед столбцом k
    total = n * m * (n * m + 1) // 2
    k_min = 0
    diff_min = total
    vertical = True

    low = m // 2
    high = m
    
    for k in range(m // 2, m + 1):
        # все суммы, это тоже арифметические прогрессии
        s1 = (((1 + k) / 2)  + ((m * (n - 1) + 1) + (m * (n - 1) + k)) / 2) * k * n / 2
        s = abs(s1 - (total - s1))
        if s < diff_min:
            k_min = k + 1 # нумерация с одного
            vertical = True
            diff_min = s
    for j in range(n // 2, n + 1):
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
