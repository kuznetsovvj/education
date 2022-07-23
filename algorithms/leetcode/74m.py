# https://leetcode.com/problems/search-a-2d-matrix/

import bisect

def searchMatrix(matrix, target):
    row = bisect.bisect([matrix[i][0] for i in range(len(matrix))], target)
    if row == 0:
        return False
    else:
        column = bisect.bisect(matrix[row-1], target)
        if column == 0:
            return False
        return matrix[row-1][column-1] == target


assert searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3) == True
assert searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13) == False
assert searchMatrix(matrix = [[10, 12, 13]], target = 2) == False

