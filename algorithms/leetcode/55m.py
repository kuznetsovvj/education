# https://leetcode.com/problems/jump-game/
# 55. Jump Game

# Medium

def solution(nums):
    if len(nums) == 1:
        return True
    pos = len(nums) - 2
    value = 1
    while pos > 0:
        if nums[pos] >= value:
            value = 1
        else:
            value += 1
        pos -= 1
    return nums[0] >= value


assert solution([2,3,1,1,4]) == True
assert solution([3,2,1,0,4]) == False
assert solution([1]) == True
assert solution([1,2]) == True
assert solution([0,2]) == False
