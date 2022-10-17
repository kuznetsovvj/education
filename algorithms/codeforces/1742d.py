# https://codeforces.com/contest/1742/problem/D

from collections import defaultdict


def euclid(a, b):
    a, b = min(a, b), max(a, b)
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b

# Решение в лоб - timelimit
def check(seq):
    m = -1
    for i in range(len(seq) - 1, -1, -1):
        for k in range(i, -1, -1):
            if i + k < m:
                break
            if euclid(seq[i], seq[k]) == 1:
                m = max(m, i + k)
    if m != -1:
        m += 2
    return m

# С помощью подсказки, элементы массива меньше 1000, их проще перебрать
def advanced_check(seq):
    d = defaultdict(int)
    # храним максимальный номер массива
    for idx, item in enumerate(seq):
        d[item] = idx + 1

    m = -1
    for item in d.keys():
        for pair in d.keys():
            if euclid(item, pair) == 1:
                m = max(m, d[item] + d[pair])
    return m

t = int(input())
for _ in range(t):
    input()
    seq = tuple(map(int, input().split()))
    print(advanced_check(seq))
