# https://leetcode.com/problems/surface-area-of-3d-shapes/description/

def surfaceArea(grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                res += 2 # дно и крышка
            # верх
            if i == 0:
                res += grid[i][j] 
            else:
                if grid[i][j] > grid[i-1][j]:
                    res += grid[i][j] - grid[i-1][j]
            # низ
            if i == len(grid) - 1:
                res += grid[i][j] 
            else:
                if grid[i][j] > grid[i+1][j]:
                    res += grid[i][j] - grid[i+1][j]
            # право
            if j == len(grid[i]) - 1:
                res += grid[i][j]
            else:
                if grid[i][j] > grid[i][j+1]:
                    res += grid[i][j] - grid[i][j+1]
            # лево
            if j == 0:
                res += grid[i][j]
            else:
                if grid[i][j] > grid[i][j-1]:
                    res += grid[i][j] - grid[i][j-1]
    return res

assert surfaceArea([[1,2], [3,4]]) == 34
assert surfaceArea([[1,1,1], [1,0,1], [1,1,1]]) == 32
assert surfaceArea([[2,2,2], [2,1,2], [2,2,2]]) == 46