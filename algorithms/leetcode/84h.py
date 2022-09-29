# https://leetcode.com/problems/largest-rectangle-in-histogram/

# Алгоритм сложность O(n^2)
# С помощью таблички вычисляем минимум "высоты" для каждого отрезка
# а затем, выясняем его "площадь"


# решение правильное, но не пролезло по памяти 
# ок, будем держать в памяти только последнюю строку
def solution(heights):
    l = len(heights)
    res, m = 0, [[None for _ in range(l)] for _ in range(l)]

    for idx, item in enumerate(heights):
        m[idx][idx] = heights[idx]
    
    for k in range(l):
        for j in range(k,-1,-1):
            if k == j:
                res = max(res, heights[k])
                continue
            m[k][j] = min(m[k-1][j], m[k][j+1])
            res = max(res, m[k][j] * (k - j + 1))

    return res

# ок, решение правильное, но не пролезло по времени :(
def solution2(heights):
    l = len(heights)
    res, m = heights[0], [heights[0]]
   
    for k in range(1, l):
        tmp, res = [heights[k]], max(res, heights[k])
        for idx, item in enumerate(m):
            z = min(tmp[-1], item)
            res = max(res, z * (idx + 2))
            tmp.append(z)
        m = tmp
    return res

# Решение за O(n) пока еще предстоит придумать

assert solution2([2,1,5,6,2,3]) == 10
assert solution2([2,4]) == 4
            

            
            
