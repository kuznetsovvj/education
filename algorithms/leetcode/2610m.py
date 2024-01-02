# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions

def findMatrix(nums):
    cnt = {}
    res = [[]]
    for num in nums:
        if num not in cnt:
            cnt[num] = 1
            res[0].append(num)
        else:
            cnt[num] += 1
            if len(res) < cnt[num]:
                res.append([num])
            else:
                res[cnt[num]-1].append(num)
    return res

print(findMatrix(nums = [1,3,4,1,2,3,1]))