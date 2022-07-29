# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

def search(nums, target):
    if target == nums[0]:
        return True
    
    for i in range(1, len(nums)):
        if nums[i] == target:
            return True

        if nums[i] > target:
            break

        if nums[i] < target:
            if nums[i] < nums[i-1]:
                break
        
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == target:
            return True
        
        if nums[i] < target:
            return False
        
        if nums[i] > target:
            if nums[i] < nums[i-1]:
                return False
    
    return False

assert search([2, 5, 6, 0, 0, 1, 2], 0) == True