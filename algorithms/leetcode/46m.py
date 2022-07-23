# https://leetcode.com/problems/permutations/
# leetcode 46
# medium

# Использовать itertools.permutation неспортивно
# Задача 2.2.1. Шень "Программрование: теоремы и задачи"
import copy


# Результат: переводим перестановки индексов в перестановку элементов исходного массива
def add_result(nums, idxs):
    return [nums[i] for i in idxs]


def solution(nums):
    res = []
    # Будем генерировать комбинаторные перестановки индексов элементов в исходном массиве
    idxs = list(range(len(nums)))
    res.append(add_result(nums, idxs))
    # Первоначальная последовательность 0, 1, 2, 3... n-1
    # Ищем такую k, что хотя бы один элемент после него - меньше k
    while True:
        k = len(nums) - 2
        while idxs[k] > idxs[k+1]:
            k = k - 1
        # если поменять ничего уже нельзя - работа закончена
        if k == -1:
            break
        # Теперь ищем такое t, которое можно будет обменять с k
        t = k + 1
        while t < len(nums) - 1 and idxs[t + 1] > idxs[k]:
            t = t + 1
        idxs[k], idxs[t] = idxs[t], idxs[k]
        # перестановка элементов от k+1 до конца в обратном порядке
        idxs[k+1:] = idxs[len(nums) - 1: k:-1]
        res.append(add_result(nums, idxs))
    return res

print(solution([1,2,3]))
