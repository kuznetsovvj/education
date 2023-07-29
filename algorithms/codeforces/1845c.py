# https://codeforces.com/contest/1845/problem/C

# Чудовищно переусложнил решение
# Хотел строить граф с основанием 10 

# Алгортм подсмотрел в edutorial

def check(s, m1, m2):
    # разряд, текущая позиция в s, длина пароля
    t, pos, l = 0, -1, len(m1)
    while True:
        keys = [key for key in range(int(m1[t]), int(m2[t])+1)]
        dic = {key:len(s)+2 for key in keys}
        for i in range(pos+1, len(s)):
           k = int(s[i])
           if k in dic and dic[k] == len(s) + 2:
               dic[k] = i
        if max(dic.values()) == len(s) + 2:
            return "YES"
        else:
            pos = max(dic.values())
            t += 1
        if t == l:
            return "NO"

for _ in range(int(input())):
    s, _, m1, m2 = input(), input(), input(), input()
    print(check(s, m1, m2))