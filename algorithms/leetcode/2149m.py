# https://leetcode.com/problems/rearrange-array-elements-by-sign

def rearrangeArray(nums):
    from collections import deque
    nd, pd = deque([]), deque([])
    for item in nums:
        if item < 0:
            nd.append(item)
        else:
            pd.append(item)
    for i in range(len(nums)):
        if i % 2 == 0:
            nums[i] = pd.popleft()
        else:
            nums[i] = nd.popleft()
    return nums

print(rearrangeArray([3,1,-2,-5,2,-4]))

