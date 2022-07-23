"""https://codeforces.com/contest/1352/problem/G"""
"""Сложность: 1600"""

"""Перестановкой длины n называется такой массив p=[p1,p2,…,pn], 
который содержит каждое число от 1 до n (включительно) и притом ровно по одному разу. Например, p=[3,1,4,2,5] — перестановка длины 5.

Для заданного числа n (n≥2) найдите такую перестановку p, 
в которой разница (то есть модуль разности) любых двух соседних элементов находится в диапазоне от 2 до 4, 
включительно. Формально, для перестановки p должно выполняться 2≤|pi−pi+1|≤4 для всех i (1≤i<n).

Выведите любую такую перестановку для заданного значения n или определите, что ее не существует."""

# Решение
""" Для n = 1, 2, 3 - решений нет
Для n = 4k, решение разбиваются на четверки вида (2, 4, 1, 3)
Для n = 4k + 1 последняя четверка будет иметь вид (2, 4, 1, 3, 5)
Для n = 4k + 2 последняя четверка будет иметь вид (2, 5, 3, 6, 4, 1)
Для n = 4k + 3 последняя четверка будет иметь вид (2, 6, 4, 1, 3, 5, 7)"""

def solution(n):
    if n <= 3:
        print("-1")
        return
    res = []
    for k in range(1, n // 4):
        res.append(4 * k - 2)
        res.append(4 * k)
        res.append(4 * k - 3)
        res.append(4 * k - 1)
    z = n // 4
    if n % 4 == 0:
        res.append(4 * z - 2)
        res.append(4 * z)
        res.append(4 * z - 3)
        res.append(4 * z - 1)
    if n % 4 == 1:
        res.append(4 * z - 2)
        res.append(4 * z)
        res.append(4 * z - 3)
        res.append(4 * z - 1)
        res.append(4 * z + 1)
    if n % 4 == 2:
        res.append(4 * z - 2)
        res.append(4 * z + 1)
        res.append(4 * z - 1)
        res.append(4 * z + 2)
        res.append(4 * z)
        res.append(4 * z - 3)
    if n % 4 == 3:
        res.append(4 * z - 2)
        res.append(4 * z + 2)
        res.append(4 * z)
        res.append(4 * z - 3)
        res.append(4 * z - 1)
        res.append(4 * z + 1)
        res.append(4 * z + 3)
    print(' '.join(map(str,res)))


inp = int(input())
for _ in range(inp):
    n = int(input())
    solution(n)