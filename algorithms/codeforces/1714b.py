# https://codeforces.com/contest/1714/problem/B

def check(nums):
    t = set()
    for i in range(len(nums)-1, -1, -1):
        if nums[i] in t:
            return i + 1
        t.add(nums[i])
    return 0

t = int(input())
for _ in range(t):
    input()
    nums = tuple(map(int, input().split()))
    print(check(nums))


check([3,1,4,3]) == 1
check([1,1,1,1,1]) == 4
check([1]) == 0
check([1,2,3,4,5]) == 0
check([1,2,3,4,5,6,2]) == 2
