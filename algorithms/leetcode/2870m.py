# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

def minOperations(nums):
    cnt = {}
    for i in nums:
        if i not in cnt:
            cnt[i] = 1
        else:
            cnt[i] += 1
    res = 0
    for v in cnt.values():
        if v == 1:
            return -1
        if v % 3 == 0:
            res += v // 3
        if v % 3 == 2:
            res += v // 3 + 1
        if v % 3 == 1:
            res += 2 + (v - 4) // 3
    return res

assert minOperations(nums = [2,3,3,2,2,4,2,3,4]) == 4
assert minOperations(nums = [2,1,2,2,3,3]) == -1
            