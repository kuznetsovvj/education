# https://leetcode.com/problems/spiral-matrix/
# 54. Spiral Matrix

# Medium

def solution(matrix):
    trace = ((0, 1), (1, 0), (0, -1), (-1, 0))
    row_up, row_down = 0, len(matrix) - 1
    col_left, col_right = 0, len(matrix[0]) - 1

    res = []
    crt = [0, 0]
    current_trace = 0
    while len(res) != len(matrix) * len(matrix[0]): 
        res.append(matrix[crt[0]][crt[1]])
        if (row_up <= crt[0] + trace[current_trace][0] <= row_down) and (col_left <= crt[1] + trace[current_trace][1] <= col_right):
            crt[0] = crt[0] + trace[current_trace][0]
            crt[1] = crt[1] + trace[current_trace][1]
        else:
            if current_trace == 0:
                current_trace = 1
                row_up += 1
            elif current_trace == 1:
                current_trace = 2
                col_right -= 1
            elif current_trace == 2:
                current_trace = 3
                row_down -= 1
            else:
                current_trace = 0
                col_left += 1
            crt[0] = crt[0] + trace[current_trace][0]
            crt[1] = crt[1] + trace[current_trace][1]
    return res

assert solution([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
assert solution([[1,2,3,4]]) == [1,2,3,4]
assert solution([[1],[2],[3],[4]]) == [1,2,3,4]
assert solution([[1,2,3,4],[5,6,7,8]]) == [1,2,3,4,8,7,6,5]
assert solution([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]