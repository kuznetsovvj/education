# https://leetcode.com/problems/house-robber

def rob(nums):
    d, n = [0 for _ in range(len(nums))], [0 for _ in range(len(nums))]
    d[0] = nums[0]
    for i in range(1, len(nums)):
        d[i] = n[i-1] + nums[i]
        n[i] = max(d[i-1], n[i-1])
    return max(d[-1], n[-1])

assert rob([1,2,3,1]) == 4
assert rob([2,7,9,3,1]) == 12
assert rob([1,40,1,1,40]) == 80