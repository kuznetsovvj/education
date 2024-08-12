# https://leetcode.com/problems/kth-largest-element-in-a-stream/?envType=daily-question&envId=2024-08-12

import bisect


class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        nums.sort()
        if k > len(nums):
            self.arr = nums
        else:
            self.arr = nums[len(nums)-k:]
    
    def add(self, val: int) -> int:
        bisect.insort_left(self.arr, val)
        if len(self.arr) > self.k:
            del self.arr[0]
        return self.arr[0]
    

s = KthLargest(3,[4,5,8,2])
print(s.add(3))
print(s.add(5))
print(s.add(10))
print(s.add(9))
print(s.add(4))
