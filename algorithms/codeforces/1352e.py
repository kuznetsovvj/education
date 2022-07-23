"""https://codeforces.com/contest/1352/problem/E"""
"""Сложность: 1500"""

"""Задан массив a=[a1,a2,…,an] (1≤ai≤n). Его элемент ai называется особым, если существует такая пара индексов l и r (1≤l<r≤n), 
что ai=al+al+1+…+ar. Иными словами, элемент называется особым, если он представим в виде суммы двух или более подряд идущих элементов массива 
(не важно, особых или нет).

Выведите количество особых элементов заданного массива a."""

# Решение 1 - ERROR: Превышено потребление памяти
"""
Пример массив [3, 1, 4, 1, 5, 9, 2, 6, 5]
S0 - предыдущий символ, Sk - суммы, которые закончились, St - суммы, которые продолжаются
idx 1, value 1, S0 + value = 4. St = [4]
idx 2, value 4, Sk = St = [4], Прибавляем value ко всем значениям St, St = [8]. S0 + value -> St, St = [5, 8]
idx 3, value 1, Sk = Sk + St = [4, 5, 6]. value + St = [6, 9]. S0 + value -> St, St = [5, 6, 9]
"""

def solution(a):
    cnt = 0
    s_ended, s_cont = set(), set()
    for idx, item in enumerate(a):
        if idx == 0:  # для первого значения только сохранить его в "предыдущее"
            prev = item
            continue
        s_ended.update(s_cont)  # все значения с прошлого шага перевести в завершенные
        new_s_cont = set()
        for elem in s_cont:
            new_s_cont.add(elem + item)  # ко всем текущим добавить item
        new_s_cont.add(prev + item)  # новая сумма из двух элементов
        s_cont = new_s_cont
        prev = item 
    for item in a:
        if item in s_ended or item in s_cont:
            cnt += 1
    print(cnt)


# Решение 2 (Прочитал разбор задачи на сайте)

import collections


def solution1(a):
    cnt = 0
    max_ = max(a)  # максимальное значение элемента в исходном массиве
    c = collections.Counter(a)  # подсчет кол-ва встречаемости элемента в исходном массиве
    cur_sum = 0
    for right_border in range(len(a)-1): # правая граница "окна"
        cur_sum = a[right_border]
        for left_border in range(right_border + 1, len(a)): # левая граница "окна"
            cur_sum += a[left_border]
            if c[cur_sum] != 0:  # если в массиве есть элементы == текущей сумме - добавить их количество в ответ
                cnt += c[cur_sum] 
                c[cur_sum] = 0  # эти элементы мы уже посчитали, теперь их 0
            if cur_sum > max_:  # если текущая сумма превзошла максимальный элемент - то дальше считать не надо
                break 
    print(cnt)


inp = int(input())
for _ in range(inp):
    _ = input()
    input_ = tuple(map(int, input().split()))
    solution1(input_)
