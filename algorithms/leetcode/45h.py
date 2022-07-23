# https://leetcode.com/problems/jump-game-ii/
# leetcode 45
# hard


def solution(nums):
    if len(nums) == 1:
        return 0

    threshold, step = 0, 1
    current_treshold = nums[0]
    for i in range(len(nums)):
        if i + nums[i] >= len(nums) - 1:
            return step
        if i == threshold:
            step += 1
            threshold = max(current_treshold, i + nums[i])
        else:
            if i + nums[i] > current_treshold:
                current_treshold = i + nums[i]


assert solution([1,1,1,1]) == 3
assert solution([2,3,1,1,4]) == 2
assert solution([4,1]) == 1
assert solution([1,1,1,1,1]) == 4

    


