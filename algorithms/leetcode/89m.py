# https://leetcode.com/problems/gray-code/

# Коды Грея описаны в учебнике Шеня
# Простой способ их генерации: записать последовательность чисел по порядку от 0 до 2^n - 1 в двоичном виде
# Затем каждую цифру числа, кроме первой заменить на её сумму с предыдущей по модулю 2

# Наркоманское решение на строках
def solve(n):
    z = (bin(i) for i in range(2**n))
    res = []
    if n != 1:
        for item in z:
            tmp = item[:3]
            for z in range(3,len(item)):
                tmp += str((int(item[z]) + int(item[z-1])) % 2)
            res.append(tmp)
    else:
        res = z
    return [int(i, 2) for i in res]

# Конечно, надо решить красиво с битовыми сдвигами, но потом