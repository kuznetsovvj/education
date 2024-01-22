# https://leetcode.com/problems/set-mismatch

def findErrorNums(nums):
    a = set(range(1, len(nums)+1))
    res = []
    for it in nums:
        if it in a:
            a.remove(it)
        else:
            res.append(it)
    res += list(a)
    return res

print(findErrorNums([1,2,2,4]))
print(findErrorNums([1,1]))
    