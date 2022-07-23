# https://leetcode.com/problems/unique-paths-ii/
# 63. Unique Paths II

# Medium

def solution(obstacleGrid):
    if (obstacleGrid[0][0] == 1):
        return 0
    mtx = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if obstacleGrid[i][j] != 0:
                mtx[i][j] = 0
            else:
                if i == 0 and j == 0:
                    mtx[i][j] = 1
                elif i == 0:
                    mtx[i][j] = mtx[i][j-1]
                elif j == 0:
                    mtx[i][j] = mtx[i-1][j]
                else:
                    mtx[i][j] = mtx[i][j-1] + mtx[i-1][j]
    
    return mtx[-1][-1]

assert solution([[0,0,0],[0,1,0],[0,0,0]]) == 2
assert solution([[0,1],[0,0]]) == 1
assert solution([[0,0,0],[0,0,0],[0,0,0]]) == 6
assert solution([[0,1],[1,0]]) == 0

    
    