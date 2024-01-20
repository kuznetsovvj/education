# https://leetcode.com/problems/minimum-falling-path-sum

def minFallingPathSum(matrix):
    sums = [[None for i in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix[0])):
        sums[0][i] = matrix[0][i]

    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            center = sums[i-1][j]
            if j == 0:
                left = 100000000000000000000000000
            else:
                left = sums[i-1][j-1]
            if j == len(matrix[0]) - 1:
                right = 100000000000000000000000000
            else:
                right = sums[i-1][j+1]
            
            mx = min(center, left, right)
            sums[i][j] = mx + matrix[i][j]
    
    return min(sums[-1])

assert minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]) == 13
assert minFallingPathSum([[-19,57],[-40,-5]]) == -59


                
    
            
    