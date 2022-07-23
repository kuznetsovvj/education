# https://leetcode.com/problems/n-queens/
# 51. n-queens

# hard

# Задача аналогична Шень 3.1.1.
from collections import defaultdict
from itertools import chain
import copy


def check(current_position):
    vertical = defaultdict(int)
    pos_diag = defaultdict(int)
    neg_diag = defaultdict(int)
    for idx,item in enumerate(current_position):
        if item != -1:
            vertical[item] += 1
            pos_diag[idx + item] += 1
            neg_diag[idx - item] += 1
    for val in chain(vertical.values(), pos_diag.values(), neg_diag.values()):
        if val > 1:
            return False
    return True


def solution(n):
    # Перечень решений
    result = []
    # Текущее решение
    current_position = [-1 for i in range(n)]
    # Текущий номер ферзя
    current_queen = 0
    # Флаг окончания перебора
    end_flag = False

    while not end_flag:
        # перешли к новому ферзю
        if current_position[current_queen] == -1:

            # ставим ферзя 
            current_position[current_queen] = 0
            if check(current_position):
                if current_queen == n-1:
                    result.append(copy.deepcopy(current_position))
                else:
                    current_queen += 1 
                # все ок, надо переходить к следующему
            # не ок
            continue
            
        if current_position[current_queen] != n - 1:
            current_position[current_queen] += 1
            if check(current_position):
                if current_queen == n-1:
                    result.append(copy.deepcopy(current_position))
                else:
                    current_queen += 1 
            continue

        if current_position[current_queen] == n-1:
            if current_queen != 0:
                current_queen -= 1
                for j in range(current_queen + 1, n):
                    current_position[j] = -1
            else:
                end_flag = True
    
    output = []
    for res in result:
        z = []
        for i in res:
            t = "." * i + "Q" + "." * (n - 1 - i)
            z.append(t)
        output.append(z)
    return output
    
            


solution(4)






