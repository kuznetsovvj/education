"""https://codeforces.com/contest/1360/problem/E"""
"""Сложность: 1300"""

"""Задание с картинками, без них понять тяжело, смотри ссылку"""

# Решение
"""Надо проверить, если у каждой единицы на ячейке справа/снизу или есть 1, или край карты - то ок,
если нет, то не ок"""

# Забыл про матрицу из одних нулей


import sys


def solution(a):
    for idx_row, row in enumerate(a):
        for idx_item, item in enumerate(row):
            if item == '1':
                if idx_item == len(row) - 1 or row[idx_item + 1] == '1' or\
                    idx_row == len(a) - 1 or a[idx_row + 1][idx_item] == '1':
                    continue
                else:
                    print('NO')
                    return
    print('YES')

# попытка ускорения чтения ввода - ошибка была тут :((
"""reader = (line.strip() for line in sys.stdin)
inp = tuple(reader)
current = 1
for i in range(int(inp[0])):
    cnt = int(inp[current])
    solution(inp[current:current+cnt+1])
    current += 1 + cnt"""

inp = int(input())
for _ in range(inp):
    cnt = int(input())
    res = []
    for i in range(cnt):
        res.append(input())
    solution(res)





