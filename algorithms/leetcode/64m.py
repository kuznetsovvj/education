# https://leetcode.com/problems/minimum-path-sum/
# 64. Minimum Path Sum

# Medium

def solution(grid):
    for idx_row in range(len(grid)):
        for idx_clm in range(len(grid[idx_row])):
            if idx_clm == 0 and idx_row == 0:
                continue
            prefix = []
            if idx_row > 0:
                prefix.append(grid[idx_row-1][idx_clm])
            if idx_clm > 0:
                prefix.append(grid[idx_row][idx_clm-1])
            grid[idx_row][idx_clm] += min(prefix)
    return grid[-1][-1]


assert solution(grid = [[1,3,1],[1,5,1],[4,2,1]]) == 7
assert solution(grid = [[1,2,3],[4,5,6]]) == 12
