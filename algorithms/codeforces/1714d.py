# https://codeforces.com/contest/1714/problem/D

# Идея: сначала ищем подстроку, которая начинается с 1-го символа, а потом перебираем один за другим

def check(target, patterns):
    steps = []
    # проверим, если ли вхождение на первом символе
    res, step = check_start(target, patterns)
    # res - успех или неудача, step - это кортеж, где первый - это номер шаблона, а цифра - с какой позиции в строке + 1 его применили
    if not res:
        return (-1, [])
    steps.append(step)
    # первый шаблон закончился на этом символе
    last_position = len(patterns[steps[-1][0]-1]) - 1 # отнимаем единичку - получаем номер позиции, где закончился последний шаблон
    # steps[-1][0] - 1 - потому что в ответе коллекция паттернов тоже нумеруется с 1

    last_pos = 0 # позиция, с которой мы начали последний поиск
    last_fin = last_position # позиция на который мы закончили последний шаблон
    while last_fin < len(target) - 1: # если last_fin = len() - 1 - значит все, вся строка покрыта
        res, step = check_continiously(target, patterns, last_pos, last_fin)
        if not res:
            return (-1, [])
        steps.append(step) 
        last_pos = step[1] - 1 # не забыли, что добавляли единичку для корректного ответа
        last_fin = last_pos + len(patterns[step[0]-1]) - 1 # аналогичная формула
    return (len(steps), steps)

    
def check_start(target, patterns):
    max_pos = -1 # позиция последнего символа шаблона (самого длинного префикса)
    num_pattern = -1 # номер шаблона с самым длинным префиксом
    for idx, pattern in enumerate(patterns):
        if target.startswith(pattern):
            if max_pos < len(pattern):
                max_pos = len(pattern) - 1
                num_pattern = idx + 1
    if max_pos == -1:
        return (False, None)
    return (True, (num_pattern, 1)) # мы возвращаем номер позиции в исходной строке + 1, к которой применился шаблон

def check_continiously(target, patterns, prev_start, prev_fin):
    # prev_start - номер в строке, с которого мы начали последний шаблон
    # prev_fin - номер в строке, на котором закончился последний шаблон
    max_pos = prev_fin # по умолчанию - максимальная позиция - это конец предыдущего шаблона, меньше него нет смысла пробовать
    num_pattern = -1 # номер текущего максимального паттерна
    st_pos = -1 # стартовая позиция текущего паттерна
    for pos in range(prev_start + 1, prev_fin + 2): 
        # надо перебрать позиции от prev_start + 1
        # и дойти до prev_fin + 1 - паттерны могут идти "в стык", без наложения
        for idx, pattern in enumerate(patterns):
            if target.startswith(pattern, pos): # ищем вхождение паттерна с позиции pos
                if max_pos < len(pattern) + pos - 1: # паттерн начинается на символе 4 и длиной 2 - значит позиция окончания 5, верно
                    max_pos = len(pattern) + pos - 1
                    st_pos = pos # стартовая позиция паттерна c нуля!
                    num_pattern = idx + 1 # номер шаблона в коллекции шаблонов
    if max_pos == prev_fin: # не нашли шаблон длиннее, чем конец прошлого - тупик
        return (False, None)
    return (True, (num_pattern, st_pos + 1)) # если мы делаем позицию для ответа - то строка нумерация с 1, +1



t = int(input())
for _ in range(t):
    target = input()
    tt = int(input())
    patterns = []
    for __ in range(tt):
        patterns.append(input())
    result, steps = check(target, patterns)
    print(result)
    if steps:
        for step in steps:
            print(f"{step[0]} {step[1]}")


assert check("bababa", ["ba", "aba"])[0] == 3
assert check("caba", ["bac", "acab"])[0] == -1
assert check("abacabaca", ["aba", "bac", "aca"])[0] == 4
