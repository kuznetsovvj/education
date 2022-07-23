# https://leetcode.com/problems/subsets/

# Вывести все подмножества перечисления
# Можно читерски решить через itertools, но это не интересно

def subsets(nums):
    mask = [0 for i in range(len(nums))]
    result = []
    # пустой массив добавим явно, не будем мучить сборку по маске
    result.append([])
    while True:
        # находим самый правый ноль
        right = -1
        for z in range(len(nums)-1, -1, -1):
            if not mask[z]:
                right = z
                break
        # вся маска состоит из одних единиц, работа закончена
        if right == -1:
            break
        # меняем крайний правый ноль на единицу
        mask[z] = 1
        # а все, что правее него - сбрасываем в ноль
        for k in range(z + 1, len(nums)):
            mask[k] = 0
        # собираем результат по маске
        result.append(collect_result(nums, mask))
    return result


def collect_result(nums, mask):
    return [nums[i] for i in range(len(nums)) if mask[i]]
    
# проверим, что функция сбора ответа по маске не скосячила
assert collect_result([1, 2, 3], [0, 0, 0]) == []
assert collect_result([1, 2, 3], [0, 0, 1]) == [3]
assert collect_result([1, 2, 3], [0, 1, 0]) == [2]
assert collect_result([1, 2, 3], [1, 0, 0]) == [1]
assert collect_result([1, 2, 3], [0, 1, 1]) == [2, 3]
assert collect_result([1, 2, 3], [1, 0, 1]) == [1, 3]
assert collect_result([1, 2, 3], [1, 1, 0]) == [1, 2]
assert collect_result([1, 2, 3], [1, 1, 1]) == [1, 2, 3]

print(subsets([1,2,3]))
print(subsets([0]))