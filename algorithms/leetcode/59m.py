# https://leetcode.com/problems/spiral-matrix-ii/
# 59. Spiral Matrix II

# Medium

def solution(n):
    trace = ((0, 1), (1, 0), (0, -1), (-1, 0))
    row_up, row_down = 0, n - 1
    col_left, col_right = 0, n - 1

    res = [[0 for _ in range(n)] for _ in range(n)]
    crt = [0, 0]
    current_trace = 0
    for i in range(n**2):
        res[crt[0]][crt[1]] = i + 1
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
