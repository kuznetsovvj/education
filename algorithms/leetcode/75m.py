# https://leetcode.com/problems/sort-colors/

# brute-force
# two-pass algoritm
def sortColors(nums):
    d = {0:0, 1:0, 2:0}
    for item in nums:
        d[item] += 1
    for i in range(len(nums)):
        if i < d[0]:
            nums[i] = 0
            continue
        if i < d[0] + d[1]:
            nums[i] = 1
            continue
        nums[i] = 2

# one-pass 
def sortColorsOne(nums):
    # первое вхождение элемента в массив
    d = {0: None, 1: None, 2: None}
    for idx, item in enumerate(nums):
        # если на последнем текущем месте уже двойка, её не надо никуда двигать
        if item == 2:
            # но если двоек еще не было, надо отметить границу у первой двойки
            if d[2] is None:
                d[2] = idx
            continue
        # если на последнем месте единица
        if item == 1:
            # есть ли двойки?
            if d[2] is None:
                # двоек нет - двигать ничего не надо
                # но надо проверить, были ли раньше единицы?
                if d[1] is None:
                    d[1] = idx
            else:
                # двойки были
                # были ли раньше единицы?
                if d[1] is None:               
                    # единиц не было
                    # меняем местами 1 и 2
                    nums[d[2]] = 1
                    nums[idx] = 2
                    d[1] = d[2]
                    d[2] = d[2] + 1
                else:
                    # единицы были
                    nums[d[2]] = 1
                    nums[idx] = 2
                    d[2] = d[2] + 1
            continue
        # приехал нолик
        if item == 0:
            # есть и двойки, и единицы
            if not (d[1] is None) and not (d[2] is None):
                nums[idx] = 2
                nums[d[2]] = 1
                nums[d[1]] = 0
                d[2] += 1
                d[1] += 1
                if d[0] is None:
                    d[0] = 0
            # есть только двойки, но нет единиц
            if not (d[2] is None) and (d[1] is None):
                nums[idx] = 2
                nums[d[2]] = 0
                d[2] += 1
                if d[0] is None:
                    d[0] = 0
            # есть только единицы, но нет двоек
            if not (d[1] is None) and (d[2] is None):
                nums[idx] = 1
                nums[d[1]] = 0
                d[1] += 1
                if d[0] is None:
                    d[0] = 0
            # нет ни двоек, ни единиц
            if (d[1] is None) and (d[2] is None):
                if d[0] is None:
                    d[0] = 0

nums = [2,0,2,1,1,0]
sortColors(nums)
assert nums == [0,0,1,1,2,2]

nums = [2,0,2,1,1,0]
sortColorsOne(nums)
assert nums == [0,0,1,1,2,2]

nums = [2,0,1]
sortColors(nums)
assert nums == [0,1,2]

nums = [2,0,1]
sortColorsOne(nums)
assert nums == [0,1,2]

nums = [0]
sortColors(nums)
assert nums == [0]

nums = [0]
sortColorsOne(nums)
assert nums == [0]

nums = [1]
sortColors(nums)
assert nums == [1]

nums = [1]
sortColorsOne(nums)
assert nums == [1]

nums = [2]
sortColors(nums)
assert nums == [2]

nums = [2]
sortColorsOne(nums)
assert nums == [2]
   

        
