"""https://codeforces.com/contest/1360/problem/B"""
"""Сложность: 800"""

"""Перед вами стоит n спортсменов. Спортсмены пронумерованы от 1 до n слева направо. Про каждого спортсмена вы знаете его силу — спортсмен с номером i имеет силу si.
Вы хотите разделить всех спортсменов на две команды. В каждой команде должен быть хотя бы один спортсмен, и каждый спортсмен должен быть ровно в одной команде.
Вы хотите, чтобы самый сильный спортсмен из первой команды по силе как можно меньше отличался от самого слабого спортсмена из второй команды. 
Формально, вы хотите разделить спортсменов на две команды A и B так, чтобы величина |max(A)−min(B)| была как можно меньше, 
где max(A) — максимальная сила спортсмена из команды A, а min(B) — минимальная сила спортсмена из команды B.

Например, если n=5 и силы спортсменов равны s=[3,1,2,6,4], то одно из возможных разделений на команды имеет вид:

первая команда: A=[1,2,4],
вторая команда: B=[3,6].
В этом случае величина |max(A)−min(B)| будет равна |4−3|=1. Этот пример иллюстрирует один из способов оптимального разбиения на две команды.

Выведите минимальное значение |max(A)−min(B)|."""

# Решение
# Отсортировать и найти минимальную разницу между двумя рядом идущими значениями

def solution(a):
    a.sort()
    dif = float('inf')
    for idx, item in enumerate(a):
        if idx != 0:
            dif = min(dif, item - a[idx-1])
    print(dif)

inp = int(input())
for _ in range(inp):
    _ = input()
    a = list(map(int, input().split()))
    solution(a)