# https://leetcode.com/problems/sum-of-subarray-minimums/


# Итак, как это великолепие работает

# Заполняем таблицу n x n
# По строкам начало интервала, по столбцам - конец
#    3  1  4  2
# --------------
#  3|3  x  x  x
#  1|1  1  x  x
#  4|1  1  4  x
#  2|1  1  2  2
#
# В пересечении строки и столбца - ответ для каждого интервала
# Но! Заполнять ячейку за ячейкой - O(n**2) - долго!
# 
# Медитируем на таблицу - каждое число в прямоугольнике, как узнать его размер?

def sumSubarrayMins(arr) -> int:
    n = len(arr)
    left = [-1 for _ in range(n)]
    # индекс первого элемента, который меньше, чем мой и расположен левеее
    right = [n for _ in range(n)]
    # индекс первого элемента, который меньше или равен i-тому и расположен правее
    stack = []

    # поддерживаем мин-стек и идем слева-направо
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    stack = []

    # аналогично мин-стек и справа-налево
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    # i - left[i] и right[i] - i - как раз и есть размерчик нашего прямоугольника
    result = sum((i-left[i]) * (right[i]-i) * value for i, value in enumerate(arr)) % (10**9 + 7)

    return result

# наркомания на марше

assert sumSubarrayMins([3,1,2,4]) == 17
assert sumSubarrayMins([11,81,94,43,3]) == 444
                
    