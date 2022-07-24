# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

def removeDuplicates(nums):
    readpos, writepos = 1, 1
    previous = nums[readpos - 1]
    cnt = 1
    while readpos < len(nums):
        if nums[readpos] == previous:
            cnt += 1
        else:
            cnt = 1

        previous = nums[readpos]
        if cnt <= 2:
            nums[writepos] = nums[readpos]
            writepos += 1
        
        readpos += 1
    return writepos


assert removeDuplicates([1]) == 1
assert removeDuplicates([1,1]) == 2
assert removeDuplicates([1,1,1]) == 2
assert removeDuplicates([1,1,1,1]) == 2
assert removeDuplicates([1,1,1,2]) == 3
assert removeDuplicates([1,1,1,2,2]) == 4
assert removeDuplicates([1,1,1,2,2,2]) == 4

#assert removeDuplicates(nums=[1,1,1,2,2,3]) == 5
#assert removeDuplicates(nums=[1,2,3,4,5]) == 5
#assert removeDuplicates([1]) == 1
#assert removeDuplicates([1,1,1,1]) == 2
