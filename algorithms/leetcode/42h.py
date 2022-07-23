# https://leetcode.com/problems/trapping-rain-water/
# leetcode 42
# hard

def trap(height):
    # максимальная высота стенки, которая встречается правее местоположения i
    revmax = [0 for i in range(len(height))]
    for i in range(len(height)-2, -1, -1):
        revmax[i] = max(revmax[i+1], height[i+1])
    idx, res = 0, 0
    while idx < len(height):
        # начинаем с поиска "левого борта", если его высота 0 - то это не борт
        if height[idx] == 0:
            idx += 1
            continue
        # левый борт есть
        else:
            # ищем правый борт
            lvl = min(height[idx], revmax[idx])
            # правого борта нет, возвращает накопленное значение
            if lvl == 0:
                return res
            # правый борт есть
            else:
                idx += 1
                while i < len(height) and height[idx] < lvl:
                    res += lvl - height[idx]
                    idx += 1
    return res

assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert trap([1,2,3,0,3,2,1]) == 3
assert trap([0,0,0,1,0,0]) == 0