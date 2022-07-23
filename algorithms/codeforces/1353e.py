"""https://codeforces.com/contest/1353/problem/E"""
"""Сложность: 1900"""

"""Вам задана гирлянда, состоящая из n ламп. Состояния ламп описываются строкой s длины n. 
i-й символ строки si равен '0', если i-я лампа выключена, или '1', если i-я лампа включена. Вам также задано положительное целое число k.

За один ход вы можете выбрать одну лампу и изменить ее состояние (то есть включить ее, если она выключена, и наоборот).

Гирлянда называется k-периодичной, если расстояние между каждой парой соседних включенных ламп равно в точности k. 
Рассмотрим случай k=3. Тогда гирлянды «00010010», «1001001», «00010» и «0» являются хорошими, 
а гирлянды «00101001», «1000001» и «01001100» не являются хорошими. 
Заметьте, что гирлянда не является цикличной, то есть первая включенная лампа не идет после последней включенной лампы и наоборот.

Ваша задача — найти минимальное количество ходов, необходимое для того, чтобы получить k-периодичную гирлянду из заданной.
"""

# Решение
""" 1. Рассмотрим offset - сдвиги "шага гирлянды" относительно начала. Всего оффсетов - k, от 0 до k-1.
    2. Для примера k = 3, оффсет 0, должны гореть лампочки [0, 3, 6...], оффсет 1 [1, 4, 7...], оффсет 2 [2, 5, 9...]
    3. Если горит лампочка, которая не входит в оффсет, но её полюбому придется выключать
    4. Посчитаем горящие лампочки по модулям остатков при делении на [k] - это количество лампочек к выключению

    5. Теперь рассмотрим лампочки, попавшие в оффсет. Их надо привести к виду [000...]111[..00]
       Обозначим left - координату начала отрезка с "1", right - координату конца отрезка
    6. Динамически пройден по сетке - сдвигая left и right и разыскивая самый "дешевый" вариант
"""

# Не проходит по времени исполнения :(
# Идея решения с оффсетами и выключенными лампочками совпадает, но превращение в 00001111000 неэффективное
# не работает :/

def solution(a, k):
    if len(a) == 1:
        print(0)
        return
    res = {i:0 for i in range(k)}
    lights = {i:[] for i in range(k)}
    s = 0
    for idx, item in enumerate(a):
        lights[idx % k].append(int(item))
        if item == '1':
            res[idx % k] += 1
            s += 1
    min_value = float('infinity')
    for key_ in sorted(res, key=res.get, reverse=True):
        cnt = s - res[key_] # сколько потребуется переключить лампочек, не попавших в оффсет

        current_min = len(lights[key_]) - res[key_]
        current = current_min
        idx_min = len(lights[key_]) - 1
        for right in range(len(lights[key_])-2, -1, -1):
            if lights[key_][right+1] == 1:
                current += 1
            else:
                current -= 1
                if current < current_min:
                    current_min = current
                    idx_min = right
        current = current_min
        for left in range(1, idx_min+1):
            if lights[key_][left-1] == 1:
                current += 1
            else:
                current -= 1
                if current < current_min:
                    current_min = current
        if lights[key_][left] == 0:
            current -= 1
            if current < current_min:
                    current_min = current
        cnt += current_min
        if cnt < min_value:
            min_value = cnt
    print(min_value)


# Решение из разбора, основная идея та же, разбор строк 0001111000 другой

def solution2(a, k):
    # подсчет количества 1 в исходной строке // аналогично
    cnt = sum(a)
    # разбивка на оффсеты // аналогично
    offsets = [[] for _ in range(k)]
    for idx, item in enumerate(a):
        offsets[idx % k].append(item)
    # ответ по умолчанию
    res = 10**9
    # проход по оффсетам
    for offset in offsets:
        # подсчет количества 1 в оффсете
        cnt_offset = sum(offset)
        
        res = min(res, solve(offset, cnt_offset) + cnt - cnt_offset)
    print(res)


# вот тут начинается магия
def solve(offset, cnt_offset):
    n = len(offset) # длина оффсета
    ans = cnt_offset # в худшем случае - можно выключить все 1 и все будет ОК
    res = [] 
    pref = 0 # ??
    for i in range(n):
        current = offset[i]
        pref += current
        res.append(1 - current)
        if i > 0:
            res[i] += min(res[i - 1], pref - current)
        ans = min(ans, res[i] + cnt_offset - pref)
    return ans


# Так и не сдал эту задачу: python не пролезает по скорости
# Все равно не понял идею решения, отстой :((


inp = int(input())
for _ in range(inp):
    _, k = tuple(map(int, input().split()))
    a = tuple(map(int,input().split('')))
    solution2(a, k)