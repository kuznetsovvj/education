# https://leetcode.com/problems/set-matrix-zeroes/

def setZeroes(matrix):
    lines, columns = set(), set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                lines.add(i)
                columns.add(j)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in lines or j in columns:
                matrix[i][j] = 0
    