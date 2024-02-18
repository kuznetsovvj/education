import bisect

input()
nums = tuple(map(int, input().split()))
req = tuple(map(int, input().split()))

for r in req:
    s = bisect.bisect_left(nums, r)
    if s == 0:
        print(nums[s])
    elif s == len(nums):
        print(nums[s-1])
    else:
        if abs(nums[s-1] - r) > abs(nums[s] - r):
            print(nums[s])
        else:
            print(nums[s-1]) 
            