"""https://codeforces.com/contest/1353/problem/D"""
"""Сложность: 1600"""

"""Вам задана массив a длины n, состоящий из нулей. Вы выполняете n действий с этим массивом: 
в течение i-го действия происходит следующая последовательность операций:

Выбирается максимальный по длине подмассив (последовательный подотрезок), состоящий только из нулей, 
среди всех таких отрезков выбирается самый левый;
Пусть этот отрезок равен [l;r]. Если r−l+1 нечетно (не делится на 2), 
то присваивается a[(l+r)/2]:=i (где i — номер текущего действия), иначе (если r−l+1 четно) присваивается a[(l+r−1)/2]:=i.

Рассмотрим массив a длины 5 (изачально a=[0,0,0,0,0]). Тогда он меняется следующим образом:

Сначала мы выбираем отрезок [1;5] и присваиваем a[3]:=1, таким образом a становится равен [0,0,1,0,0];
затем мы выбираем отрезок [1;2] и присваиваем a[1]:=2, таким образом a становится равен [2,0,1,0,0];
затем мы выбираем отрезок [4;5] и присваиваем a[4]:=3, таким образом a становится равен [2,0,1,3,0];
затем мы выбираем отрезок [2;2] и присваиваем a[2]:=4, таким образом a становится равен [2,4,1,3,0];
и наконец мы выбираем отрезок [5;5] и присваиваем a[5]:=5, таким образом a становится равен [2,4,1,3,5].
Ваша задача — найти массив a длины n после выполнения всех n действий.
"""

import functools
import heapq


class Section:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.size = right - left
        if (right - left + 1) % 2 != 0:
            self.aim = (left + right) // 2  # то, куда будет вписываться число по условию
        else:
            self.aim = (left + right - 1) // 2

    @functools.total_ordering
    def __lt__(self, other):
        if self.size > other.size: # в куче, меньший отрезок тот, в котором "больше нулей", то есть больше size
            return True
        if self.size < other.size:
            return False
        return self.left < other.left # если длины равны, то берем более левый, то чем меньше left, тем "меньше" отрезок

    @functools.total_ordering
    def __eq__(self, other):
        return self.size == other.size and self.left == self.right


def solution(n):
    h = []
    res = [0 for i in range(n)]
    cnt = 1
    sec = Section(0, n - 1)
    heapq.heappush(h, sec) # добавили в кучу первый отрезок, потому что все нули
    while len(h) > 0:
        current = heapq.heappop(h) # вытащили самый длинный левый отрезок с нулями
        res[current.aim] = cnt # присвоили в ответ номер операции
        cnt += 1
        if current.left != current.aim: # если левый отрезок не вырожденный, добавили его в кучу
            new_sec1 = Section(current.left, current.aim - 1)
            heapq.heappush(h, new_sec1)
        if current.right != current.aim: # тоже самое с правым
            new_sec2 = Section(current.aim + 1, current.right)
            heapq.heappush(h, new_sec2)
    print(' '.join(map(str, res)))


inp = int(input())
for _ in range(inp):
    n = int(input())
    solution(n)