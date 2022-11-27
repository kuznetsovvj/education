# https://codeforces.com/problemset/problem/313/B

# Заведем отдельный массив, где предпосчитаем значение суммы Si для каждого i накопительным итогом
# При запросе просто будем вычитать значение массива с индексом в правом конце запроса из значения массива с индексом в левом конце

# Решение на input() тоже правильное, но медленное в реализации
"""w = input()
s = [0 for _ in range(len(w))]
for i in range(len(w)):
    if i == len(w) - 1:
        s[i] = s[i-1]
    else:
        if i == 0:
            if w[i] == w[i+1]:
                s[i] = 1
                continue
        else:
            if w[i] == w[i+1]:
                s[i] = s[i-1] + 1
            else:
                s[i] = s[i-1]
s.append(0)

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(s[r-2] - s[l-2])
"""

import sys


def check(w, cmds):
    s = [0 for _ in range(len(w))]
    for i in range(len(w)):
        if i == len(w) - 1:
            s[i] = s[i-1]
        else:
            if i == 0:
                if w[i] == w[i+1]:
                    s[i] = 1
                    continue
            else:
                if w[i] == w[i+1]:
                    s[i] = s[i-1] + 1
                else:
                    s[i] = s[i-1]
    s.append(0)

    for cmd in cmds:
        r = int(cmd[1])
        l = int(cmd[0])
        print(s[r - 2] - s[l - 2])

readl = tuple(line.split() for line in sys.stdin)
check(readl[0][0], readl[2:])
