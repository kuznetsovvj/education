# https://leetcode.com/problems/majority-element/

def majorityElement(nums):
    from collections import defaultdict
    k = len(nums) // 2
    d = defaultdict(int)
    for item in nums:
        d[item] += 1
        if d[item] > k:
            return item
        
assert majorityElement([3,2,3]) == 3
assert majorityElement([2,2,1,1,1,2,2]) == 2
