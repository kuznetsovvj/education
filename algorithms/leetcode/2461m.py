# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

def maximumSubarraySum(nums, k):
    left, right = 0, 0
    m = 0
    curr_s = nums[right]
    curr = set()
    curr.add(nums[right])
    while right < len(nums):
        while right - left + 1 < k:
            right += 1
            if right == len(nums):
                return m
            curr_s += nums[right]        
            while nums[right] in curr and left < len(nums):
                curr.remove(nums[left])
                curr_s -= nums[left]
                left += 1
            curr.add(nums[right])
        m = max(m, curr_s)
        curr.remove(nums[left])
        curr_s -= nums[left]
        left += 1
    return m

assert maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3) == 15
assert maximumSubarraySum(nums = [4,4,4], k = 3) == 0    
assert maximumSubarraySum(nums = [1,1,1,7,8,9], k = 3) == 24