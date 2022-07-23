# https://leetcode.com/problems/permutations-ii/
# leetcode 47
# medium

# Наивное решение: использовать обычные перестановки, но для сборки решений использовать хеш-таблицу
# result: медленно, но тесты прошло

def add_result(nums, idxs):
    return tuple([nums[i] for i in idxs])


def solution(nums):
    res = set()
    # Будем генерировать комбинаторные перестановки индексов элементов в исходном массиве
    idxs = list(range(len(nums)))
    res.add(add_result(nums, idxs))
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
        res.add(add_result(nums, idxs))
    return [list(item) for item in res]

print(solution([1,1,1,2]))