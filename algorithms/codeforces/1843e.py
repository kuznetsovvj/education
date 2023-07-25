# https://codeforces.com/contest/1843/problem/E

# Основную идею (бинпоиск + префиксные суммы) подсмотрел в edutorial
# Реализация своя

import sys


def check(size, intervals, cmd):

    def check_s(n):
        # реализовать проверку, есть ли на intervals хоть один "хороший" интервал
        # подсчитать префиксную суммы и потом на ней подсчитать все отрезки
        m = [0 for _ in range(size)]
        for cm in cmd[:n+1]:
            m[int(cm)-1] = 1
        
        prefix = [0 for _ in range(size+1)]
        prefix[1] = m[0]
        for i in range(2, len(prefix)):
            prefix[i] = prefix[i-1] + m[i-1]

        for interval in intervals:
            i1, i2 = map(int, interval.split())
            if prefix[i2] - prefix[i1-1] > (i2-i1+1) // 2:
                return True
        return False

    if check_s(0):
        return 1
    
    if not check_s(len(cmd) - 1):
        return -1
          
    # реализовать бинарный поиск по cmd
    fail, suc = 0, len(cmd) - 1 # последний проваленный, первый success
    while True:
        if suc - fail == 1:
            return suc + 1
        tmp = (suc + fail) // 2
        if check_s(tmp):
            suc = tmp
        else:
            fail = tmp
    
input_ = tuple(line.strip() for line in sys.stdin)
p = 1
for _ in range(int(input_[0])):
    size, cmds = map(int, input_[p].split())
    p += 1
    intervals = input_[p:p+cmds]
    p += cmds
    q = int(input_[p])
    p += 1
    cmd = input_[p:p+q]
    p += q
    print(check(size, intervals, cmd))
