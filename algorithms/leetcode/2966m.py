# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference


def divideArray(nums, k):
    nums.sort()
    res = []
    for i in range(0, len(nums) // 3):
        if abs(nums[3*i] - nums[3*i + 2]) <= k:
            res.append([nums[3*i], nums[3*i + 1], nums[3*i + 2]])
        else:
            return []
    return res        


print(divideArray([1,3,4,8,7,9,3,5,1], 2))
print(divideArray([1,3,3,2,7,3], 3))

