# https://leetcode.com/problems/rotate-image/

# leetcode 48
# medium


def solution(matrix):
    cell = set()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            cell.add((i, j))
    while len(cell) != 0:
        idx = cell.pop()
        value = matrix[idx[0]][idx[1]]
        while True:
            new_idx = (idx[1], len(matrix) - idx[0] - 1)
            if new_idx not in cell:
                matrix[new_idx[0]][new_idx[1]] = value
                break
            else:
                new_value = matrix[new_idx[0]][new_idx[1]]
                matrix[new_idx[0]][new_idx[1]] = value
                value = new_value
                idx = new_idx
            cell.remove(new_idx)
    print(matrix)


solution([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])